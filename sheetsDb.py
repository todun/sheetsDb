import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests 
import sys

class sheetsDb:
    def __init__(self,creds):        
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds, scope)
        self.sheetService = gspread.authorize(credentials)

    def connectDb(self,url):
        self.sheet = self.sheetService.open_by_url(url)

    def createTable(self,tableName,header):
        try:
            worksheet = self.sheet.add_worksheet(title=tableName, rows="100", cols="20")
            colLen=len(header)-1
            cell_list = worksheet.range('A1:'+chr(65+colLen)+'1')
            i=0
            for cell in cell_list:
                cell.value = header[i]
                i=i+1    
            worksheet.update_cells(cell_list)
        except:
            print("Please Check Table Name! Make sure the table does not exist")

    def deleteTable(self,table):
        try:
            worksheet = self.sheet.worksheet(table)
            self.sheet.del_worksheet(worksheet)
            return True
        except:
            return False

    def save(self,table,row):
        worksheet = self.sheet.worksheet(table)
        data = worksheet.get_all_values()
        lastRow = len(data)
        colLen = len(row)-1
        cell_list = worksheet.range('A'+str(lastRow+1)+':'+chr(65+colLen)+str(lastRow+1))
        i=0
        for cell in cell_list:
            cell.value = row[i]
            i=i+1    
        worksheet.update_cells(cell_list)
    
    def findRowByNumber(self,table,row):
        worksheet = self.sheet.worksheet(table)
        rowData = worksheet.row_values(row)
        return rowData
    
    def count(self,table):
        worksheet = self.sheet.worksheet(table)
        data = worksheet.get_all_values()
        return len(data)-1

    def findAll(self,table):
        worksheet = self.sheet.worksheet(table)
        data = worksheet.get_all_values()
        del data[0]
        return data

    def deleteAll(self,table):
        try:
            worksheet = self.sheet.worksheet(table)
            rowData = worksheet.row_values(1)
            self.sheet.del_worksheet(worksheet)
            worksheet = self.sheet.add_worksheet(title=table, rows="100", cols="20")
            colLen=len(rowData)-1
            cell_list = worksheet.range('A1:'+chr(65+colLen)+'1')
            i=0
            for cell in cell_list:
                cell.value = rowData[i]
                i=i+1    
            worksheet.update_cells(cell_list)
            return True
        except:
            False

    def findOneByColumn(self,table,column,item):
        worksheet = self.sheet.worksheet(table)
        header = worksheet.row_values(1)
        i=0
        for name in header:
            if(column==name):
                break
            i+=1
        data = worksheet.get_all_values()
        for row in data:
            if(row[i]==item):
                return row
        return None

    def deleteOneByColumn(self,table,column,item):
        worksheet = self.sheet.worksheet(table)
        header = worksheet.row_values(1)
        i=0
        for name in header:
            if(column==name):
                break
            i+=1
        data = worksheet.get_all_values()
        deleteIndex=-1
        index=0
        colLen=0
        newData=[]
        for row in data:
            if(colLen<len(row)):
                colLen=len(row)
            if(row[i]==item):
                deleteIndex = index
                break
            newData.extend(row)
            index+=1
        totalLength = len(data)*colLen
        if(deleteIndex==-1):
            print("Item not present")
        else:
            for j in range(deleteIndex,len(data)-1):
                data[j]=data[j+1]
            data.pop()
            for j in range(deleteIndex,len(data)):
                newData.extend(data[j])
            cell_list = worksheet.range('A1:'+chr(65+colLen-1)+str(len(data)+1))
            k=0
            for cell in cell_list:
                if(k>=len(newData)):
                    cell.value = ""
                else:
                    cell.value = newData[k]
                k=k+1    
            worksheet.update_cells(cell_list)
        data = worksheet.get_all_values()