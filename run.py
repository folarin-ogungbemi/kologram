"""
Install Modules for the program
"""
import gspread #pip install gspread
import pandas  #pip install pandas
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
    print("Start your desired project")
    print("For Example: Vacation\n")

    project_name = input("Enter your project name here: ")
    SHEET.add_worksheet(project_name, "500", "15")

    # Add project heading
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

project_starter()