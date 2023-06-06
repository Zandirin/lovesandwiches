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

    sales_data = data_str.split(",")
    data_validation(sales_data)

def data_validation(values):
    """
    Checks that data input is the correct type
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Require 6 values to be input, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

get_sales_data()