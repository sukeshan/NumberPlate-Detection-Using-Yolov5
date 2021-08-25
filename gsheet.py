import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

def write_gsheet(vehicle ,time ,excel_row ):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('paste your json downloaded file', scope)

# authorize the clientsheet 
    
    client = gspread.authorize(creds)
    sheet = client.open('type your google sheet name exist on drive').sheet1

# get the first sheet of the Spreadsheet

    sheet.update_cell(row ,column , 'data want to store' ) 
    sheet.update_cell(row ,column , 'data want to store' )
    
