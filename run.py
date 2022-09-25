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

# collect data from user
def get_kolo_data():
    """
    Get input from user
    """
    print("Please Enter your data below\n")

    user_name = input("Enter your username: ")
    print(f"{user_name}, Welcome to kologram\n")
    print("Start your first project\n")

    # Add a new worksheet
    project_name = input("Enter your project name here: ")
    SHEET.add_worksheet(project_name, "100", "10")

    # Add project heading
    HEADER = ("date", "duration", "contribution", "expectation", "outstanding")
    project = SHEET.worksheet(project_name)
    heads = project.range('A5:E5')

    for i, head in enumerate(HEADER):
        heads[i].value = head

    project.update_cells(heads)

    print(f"Your '{project_name}' koloproject has been succesfully created")

get_kolo_data()


#data = project.get_all_records()
#pandy = pandas.DataFrame(data)
#print(pandy)


