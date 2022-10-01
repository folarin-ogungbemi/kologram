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

        project_name = input("Enter your project name here:\n").capitalize()

        if validate_project_name(project_name):
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
    calculate_outstanding_amount(project_name)

    print(f"Your '{project_name}' koloproject has been succesfully created\n")


def project_overview():
    """
    See project overview
    """
    my_project = project_search()

    if my_project == "None":
        print("\nThe project you entered does not exist!!")
        print("Please check your project list and try again")
    else:
        print("-------------------- Project Overview --------------------")
        # Code idea from Google sheets API
        response = S_VALUES.get(spreadsheetId=SHEET_ID,
                                range=my_project+"!F2:J3").execute()
        values = response.get('values', [])
        print(pandas.DataFrame(values))
        print("----------------------------------------------------------")


def project_search():
    """
    Prints the list of projects
    search out project from list
    """
    my_projects = SHEET.worksheets()
    # collect created projects in a list
    my_projects_list = []
    for project in my_projects:
        projects = project.title
        my_projects_list.append(projects)

    print("\n------ My Existing Projects ------")
    print(pandas.DataFrame(my_projects_list[1:]))
    print("----------------------------------\n")

    print("Choose desired project from above list")
    my_project = input("Enter project name here:\n").capitalize()
    i = 0
    project_found = "None"
    while i < len(my_projects_list):
        if my_project == my_projects_list[i]:
            project_found = my_project
            return project_found
        i += 1
    return project_found


def kolo_budget(data):
    """
    Get Project estimated budget from user
    """
    while True:
        print("Enter budget in numbers or decimals")
        print("For Example: '1234567890', '123.456'\n")

        pro_budget = input("Enter your estimated budget for the project:\n")
        if validate_project_budget(pro_budget, data):
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
    while True:
        print("Enter project due date like so: year, month, day.")
        print("Example: 2022,9,26\n")

        project_due_date = input("Enter project due date:\n")
        current_date = datetime.date.today()
        if validate_project_due_date(project_due_date):
            print("data is valid!")
            split_date = project_due_date.split(",")
            dated_list = []
            for i in split_date:
                my_int = int(i)
                dated_list.append(my_int)
            # convert dated_list to tuple
            dated_tup = tuple(dated_list)
            # *args idea from stackoverflow
            due_date = datetime.date(*dated_tup)
            days_left = abs(current_date - due_date).days
            # json.dumps idea from PYnative
            # serialize datetime into JSON
            date_dump = json.dumps(days_left, default=str)
            data.update('I3', date_dump.strip('"')+" days")
            break


def kolo_table(project_name):
    """
    Creates an account for each contribution made
    """
    #####################
    # Add table heading #
    #####################
    heading = ("DATE", "AMOUNT")
    project = SHEET.worksheet(project_name)
    heads = project.range('C5:D5')

    for i, head in enumerate(heading):
        heads[i].value = head

    project.update_cells(heads)

    kolo_day()


def kolo_day():
    """
    Ask if user wants to save today
    Get users periodic contribution data
    """
    while True:
        question = input("Would you like to Kolo today (y/n):\n")
        if question == 'y'.lower():
            my_project = project_search()
            if my_project == "None":
                print("\nThe project you entered does not exist!!")
                print("Please check your project list and try again")
            else:
                kolo_amount = float(input("Enter contribution amount:\n"))
                # Enter date the account was credited
                credit_date = datetime.date.today()
                # json.dumps idea from PYnative
                # serialize datetime into JSON
                date_dump = json.dumps(credit_date, default=str)
                main_dump = date_dump.strip('"')
                account = [[main_dump, kolo_amount]]
                # from Google sheets API
                S_VALUES.append(spreadsheetId=SHEET_ID,
                                range=my_project+"!C5:D5",
                                valueInputOption="USER_ENTERED",
                                insertDataOption='INSERT_ROWS',
                                body={"values": account}).execute()
                calculate_outstanding_amount(my_project)
                print("\nYour koloproject has been updated\n")
            return False
        if question == 'n'.lower():
            print("Thank you for using kologram")
            return False
        print(f"Invalid input: '{question}'. Please type y or n")


def calculate_outstanding_amount(project):
    """
    collects data from account history
    deduct total amount from budget
    update outstanding
    """
    # Get project budget value from spreadsheet
    brequest = S_VALUES.get(spreadsheetId=SHEET_ID,
                            range=project+"!H3").execute()
    breq_list = brequest.get('values', [])
    for breq in breq_list:
        b_list = [str(integer) for integer in breq]
        budget = "".join(b_list)

    total_amount = 0
    # Code from Google sheet API
    # Collect kolo_amount
    response = S_VALUES.get(spreadsheetId=SHEET_ID,
                            range=project+"!D6:D500").execute()
    values = response.get('values', [])
    for value in values:
        # code from Tutorial by Eyehunt
        s_list = [str(integer) for integer in value]
        str_amount = "".join(s_list)
        int_amount = int(str_amount)
        total_amount += int_amount

    outstanding = [[int(budget) - total_amount]]
    S_VALUES.update(spreadsheetId=SHEET_ID,
                    range=project+"!J3",
                    valueInputOption='USER_ENTERED',
                    body={"values": outstanding}).execute()


def validate_project_due_date(data):
    """
    Try checks user input.
    If user input is invalid, user corrects input
    """
    try:
        if len(data) > 10:
            raise TypeError(f"You entered too many values, {data}")
    except TypeError as err:
        print(f"\nInvalid data:{err}")
        print("Please try again!\n")
        return False
    return True


def validate_project_name(name):
    """
    Try adds a new worksheet.
    If worksheet previously exist, user must enter a different name
    """
    suggest = "unique attributes"
    try:
        SHEET.add_worksheet(name, "500", "15")
    except gspread.exceptions.APIError:
        my_projects = SHEET.worksheets()
        for exist in my_projects:
            if exist.title == name:
                print(f"Koloproject '{name}' already exist")
                print("Invalid data: Please try again\n")
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
    except ValueError:
        print(f"Budget is expected in Digits, you entered '{budget}'")
        print("Invalid Data, please try again.")
        return False
    return True


# kologram Main program
def main():
    """
    Provides user navigation option
    Execute user's command
    """
    option = None  # This will be the user's service preference
    # Code idea from Computer science, Youtube
    while True:
        # Create the option  menu
        option_criteria = "Please choose option 0, 1, 2 or 3"
        print("\nWelcome to kologram, your simple project tracker")
        print(f"To begin, {option_criteria}")
        print("------------------------------------------------")
        print("1. Start a new project")
        print("2. Save today")
        print("3. See project overview")
        print("0. Exit kologram\n")
        try:
            option = int(input("Choose an option:\n"))
        except ValueError:
            print("Invalid Input.")
        # Executing users input
        if option == 0:
            print("kologram is now exiting...")
            print("Goodbye\n")
            break
        if option == 1:
            print("Starting program ...\n")
            project_starter()
        elif option == 2:
            print("Savings block is opening ...\n")
            kolo_day()
        elif option == 3:
            print("Project overview loading ...\n")
            project_overview()
        else:
            print(f"Option is Incorrect. {option_criteria}\n")


main()
