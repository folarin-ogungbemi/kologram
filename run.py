"""
Install Modules for the program
"""
import datetime
import json
import gspread  # pip install gspread
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import pandas  # pip install pandas

# Services we need access to for the program
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

"""
Accessing our google spreadsheets data and storing
in our constant variable for modification
"""
CREDS = Credentials.from_service_account_file('creds.json')
CREDS_SCOPE = CREDS.with_scopes(SCOPE)
GSPREAD_USER = gspread.authorize(CREDS_SCOPE)
SHEET = GSPREAD_USER.open('kologram')
SHEET_ID = '10X1NwBvz4pvtKHfrLJvz0I0h-4QBr_I2NYH5IChiPME'
SERVICE = build('sheets', 'v4', credentials=CREDS)
S_VALUES = SERVICE.spreadsheets().values()


def project_starter():
    """
    Get project information from user
    """
    while True:
        print("Start your desired project")
        print("e.g: 'Vacation', 'Car', 'Lamborghini', 'Child-education'\n")

        project_name = input("Enter your project name here: ").capitalize()

        if validate_project_name(project_name):
            print("name is valid!\n")
            break

    #######################
    # Add project heading #
    #######################
    heading = ("DATE", "NAME", "BUDGET", "DUE", "OUTSTANDING")
    project = SHEET.worksheet(project_name)
    heads = project.range('F2:J2')

    for i, head in enumerate(heading):
        heads[i].value = head

    project.update_cells(heads)
    project.update('G3', project_name)
    kolo_budget(project)
    kolo_date(project)
    calculate_due_date(project)
    kolo_table(project_name)

    print(f"Your '{project_name}' koloproject has been succesfully created\n")

    print("-------------------- Project Overview --------------------")
    # Code idea from Google sheets API
    result = S_VALUES.get(spreadsheetId=SHEET_ID, range=project_name+"!F2:J3")
    response = result.execute()
    values = response.get('values', [])
    print(pandas.DataFrame(values))
    print("----------------------------------------------------------")


def kolo_budget(data):
    """
    Get Project estimated budget from user
    """
    while True:
        print("Enter budget in numbers or decimals")
        print("For Example: '1234567890', '123.456'\n")

        project_budget = input("Enter your estimated budget for the project: ")
        if validate_project_budget(project_budget, data):
            print("Data is valid!\n")
            calculate_outstanding_amount(project_budget)
            break


def kolo_date(data):
    """
    Insert date of project creation
    """
    project_date = datetime.date.today()
    # json.dumps idea from PYnative
    # serialize datetime into JSON
    date_dump = json.dumps(project_date, default=str)
    data.update_acell('F3', date_dump.strip('"'))


def calculate_due_date(data):
    """
    Ask user for project due date.
    """
    print("Enter project due date like so: year, month, day.")
    print("Example: 2022, 9, 26\n")

    project_due_date = input("Enter project due date: ").split(",")
    current_date = datetime.date.today()

    dated_list = []
    for i in project_due_date:
        my_int = int(i)
        dated_list.append(my_int)
    # convert dated_list to tuple
    dated_tup = tuple(dated_list)
    # *args idea from stackoverflow
    due_date = datetime.date(*dated_tup)
    days_left = abs(current_date - due_date).days
    # serialize datetime into JSON
    date_dump = json.dumps(days_left, default=str)
    data.update('I3', date_dump.strip('"')+" days")


def validate_project_name(name):
    """
    Try adds a new worksheet.
    If worksheet previously exist, user must enter a different name
    """
    suggest = "unique attributes"
    try:
        SHEET.add_worksheet(name, "500", "15")
    except gspread.exceptions.APIError as error:
        my_projects = SHEET.worksheets()
        for exist in my_projects:
            if exist.title == name:
                print(f"Koloproject {name} already exist")
                print(f"Invalid data: {error}\n")
                print(f"Use a prefix e.g: Second-{name} or {name} {suggest}\n")
                return False
    return True


def validate_project_budget(budget, data):
    """
    Try converts user input from string to float
    ValueError if user input is not convertible
    request re-entry
    """
    try:
        convert = float(budget)
        data.update('H3', convert)
    except ValueError as err:
        print(f"Budget is expected in Digits, you entered {budget}")
        print(f"Invalid Data: {err}, please try again.")
        return False
    return True


def kolo_day():
    """
    Ask if user wants to save today
    Get users periodic contribution data
    """
    while True:
        question = input("Would you like to Kolo today (y/n): ")
        if question == 'y'.lower():
            kolo_amount = float(input("Enter contribution amount: "))
            # Enter date the account was credited
            credit_date = datetime.date.today()
            # serialize datetime into JSON
            date_dump = json.dumps(credit_date, default=str)
            main_dump = date_dump.strip('"')
            account = [main_dump, kolo_amount]
            main = [account]
            # from Google sheets API
            S_VALUES.append(spreadsheetId=SHEET_ID,
                            range="Car!C5:D5",
                            valueInputOption="USER_ENTERED",
                            insertDataOption='INSERT_ROWS',
                            body={"values": main}).execute()

            print("Your koloproject has been updated\n")
            return False
        if question == 'n'.lower():
            print("Thank you for using kologram")
            return False
        print(f"Invalid input: '{question}'. Please type y or n")


def kolo_table(project_name):
    """
    Creates an account for each contribution made
    """
    #####################
    # Add table heading #
    #####################
    heading = ("DATE", "ANOUNT")
    project = SHEET.worksheet(project_name)
    heads = project.range('C5:D5')

    for i, head in enumerate(heading):
        heads[i].value = head

    project.update_cells(heads)

    kolo_day()


def calculate_outstanding_amount(budget):
    """
    collects data from account history
    deduct total amount from budget
    update outstanding
    """
    total_amount = 0
    # Code from Google sheet API
    # Collect kolo_amount
    response = S_VALUES.get(spreadsheetId=SHEET_ID,
                            range="Car!D6:D500").execute()
    values = response.get('values', [])
    for value in values:
        # code from Tutorial by Eyehunt
        s = [str(integer) for integer in value]
        str_amount = "".join(s)
        int_amount = int(str_amount)
        total_amount += int_amount

    outstanding = [[int(budget) - total_amount]]
    S_VALUES.update(spreadsheetId=SHEET_ID,
                    range="Car!J3",
                    valueInputOption='USER_ENTERED',
                    body={"values": outstanding}).execute()


# project_starter()

# kologram Main program
option = None  # This will be the user's service preference
# Code idea from Computer science, Youtube
while option != 0:
    # Create the option  menu
    CRITERIA = "Please choose option 0, 1, 2 or 3"
    print("\nWelcome to kologram, your simple project tracker")
    print(f"To begin, {CRITERIA}")
    print("------------------------------------------------")
    print("1. Start a new project")
    print("2. Save today")
    print("3. See project overview")
    print("0. Exit kologram\n")
    option = int(input("Choose an option: "))

    # Executing users input
    if option == 0:
        print("kologram is now exiting...")
        print("Goodbye")
        break
    if option == 1:
        print("Starting program ...\n")
    elif option == 2:
        print("Savings block is opening ...\n")
    elif option == 3:
        print("Project overview loading ...\n")
    else:
        print(f"Option is Incorrect. {CRITERIA}\n")