"""
Install Modules for the program
"""
import gspread  # pip install gspread
import pandas  # pip install pandas
from google.oauth2.service_account import Credentials

"""
Constant variable that stores the APIs needed for the program
"""
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

def project_starter():
    """
    Get project information from user
    """
    while True:
        print("Start your desired project")
        print("e.g: 'Vacation', 'Car', 'Lamborghini', 'Child-education'\n")

        project_name = input("Enter your project name here: ").capitalize()

        if validate_project_name(project_name):
            print("name is valid!")
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

    print(f"Your '{project_name}' koloproject has been succesfully created\n")
  
def kolo_budget(data):
    """
    Get Project estimated budget from user
    """
    project_budget = input("Enter your estimated budget for the project: ")
    data.update('H3', project_budget)

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


project_starter()


# wks = SHEET.worksheets()
# name_wks = wks[1].title
# print(name_wks)