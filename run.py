import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Get sales figures input by the user
    """
    print("Please enter sales data from previous day...")
    print("Data should be input as 6 numbers, separated by commas...")
    print("Example: 1,34,4,56,7,89\n")

    data_str = input("Enter your data here: ")
    print(f"The data you provided is: {data_str}")

get_sales_data()