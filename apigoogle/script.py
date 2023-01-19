from __future__ import print_function
from googleapiclient.discovery import build

from google.oauth2 import service_account
import requests

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

while True:
# The ID spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1_EIyRmQnKlLQx5mkZcfJfF3O3cSXmrgo2O1Cs5sicSA'


    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="CTR!A1:V201").execute()
    values = result.get('values',[])
    print(result)
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="CTR2!A1", valueInputOption="USER_ENTERED", body={"values":values}).execute()
    if not request:
        break
#print(request)




