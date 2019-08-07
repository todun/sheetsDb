# SheetsDb
Use Google Sheets as a datastore for your app with easy data management.

## How To Use?
- `pip install sheetsdb`
- Obtain google account credentials from [Google Developer Console](https://console.developers.google.com/project)
- follow the example below to use sheetsDb

## Functionalities
- Create a connection to database 
- Create a table with column names
- Add a new entry to any table in the database
- delete any entry from a table by matching column values
- find any entry from a table by matching column values
- get all entries in the table

## Example
```python
from sheetsDb import *

creds = {
    "type": "XXXXXXXXXXXXXXXXXXX",
    "project_id": "XXXXXXXXXXXXXXXXXXX",
    "private_key_id": "XXXXXXXXXXXXXXXXXXX",
    "private_key": "XXXXXXXXXXXXXXXXXXX",
    "client_email": "XXXXXXXXXXXXXXXXXXX",
    "client_id": "XXXXXXXXXXXXXXXXXXX",
    "auth_uri": "XXXXXXXXXXXXXXXXXXX",
    "token_uri": "XXXXXXXXXXXXXXXXXXX",
    "auth_provider_x509_cert_url": "XXXXXXXXXXXXXXXXXXX",
    "client_x509_cert_url": "XXXXXXXXXXXXXXXXXXX"
}

sheetsObj = sheetsDb(creds)
sheetsObj.connectDb("https://docs.google.com/spreadsheets/d/1k2ypyks7-4EpZmsRHBHOSm4KfplTgFFZD-SciA45DFQ")
sheetsObj.createTable("User Details",["First Name","Last Name"])
sheetsObj.save("User Details",["Aswin","VB"])
sheetsObj.save("User Details",["John","Doe"])
sheetsObj.save("User Details",["Leonardo","Dicaprio"])
data=sheetsObj.findAll("User Details")
item=sheetsObj.findOneByColumn("User Details","First Name","Aswin")
sheetsObj.deleteOneByColumn("User Details","First Name","Aswin")
sheetsObj.deleteAll("User Details")
sheetsObj.deleteTable("User Details")
```