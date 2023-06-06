import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    while True:
        print("Please enter sales data from previous day...")
        print("Data should be input as 6 numbers, separated by commas...")
        print("Example: 1,34,4,56,7,89\n")

        data_str = input("Enter your data here: ")

        sales_data = data_str.split(",")
        data_validation(sales_data)

        if data_validation(sales_data):
            print("Data is valid!")
            break

    return sales_data

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
        return False
    return True

def update_worksheet(data, worksheet):
    """
    updates worksheet and adds a row based on data input by user
    """
    print(f"Updating {worksheet} worksheet...\n")
    updated_worksheet = SHEET.worksheet(worksheet)
    updated_worksheet.append_row(data)
    print(f"{worksheet} updated successfully!\n")


def calculate_surplus_data(sales_row):
    """
    Calculates the surplus stock for each item type.
    A positive result indicates waste stock.
    A negative result indicates extra stock was made to meet demand.
    """
    print("calculating surplus data...\n")
    stock = SHEET.worksheet('stock').get_all_values()
    stock_row = stock[-1]
    
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    
    return surplus_data

def get_last_5_sales_entries():
    """
    Gets the last 5 entries of data from each column in the sales sheet
    """
    sales = SHEET.worksheet('sales')

    columns = []
    for ind in range(1, 7):
        column = sales.col_values(ind)
        columns.append(column[-5:])
    
    return columns

def main():
    """
    Main function of the program, calls all other functions and runs them to update the spreadsheet.
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, 'sales')
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, 'surplus')

print("Welcome to Love Sandwiches Data Automation")
# main()

sales_columns = get_last_5_sales_entries()