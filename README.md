# Kologram

## Introduction
Kologram is a simple project tracker programmed majorly with the use of Python programming language in connection with google sheets API to keep track of users' interested projects and store user data in google sheets. The Word Kologram is coined from the word kolo, A word well known to Nigerians as a private "Savings Box". The Application kologram intends to imitate this usage. Kologram allows its user to interact with the program by providing navigation options and input questions to collect user data. Through the usage of kologram, users are expected to better track their desired projects and contributions towards it.
[Link to live website](https://flo-kologram.herokuapp.com/ "visit website")

![Kologram](./assets/images/kologram%20mockup-c.png "Kologram Mockup")

---
# Features

## Existing Features
* Application Navigation option.
    * The application allows user to view and select from the options available for navigation purposes. These options are present at the main page and pops up at relevant times during use of application.
    ![kologram main](./assets/images/kologram%20navigation-c.png "view image")
* Input Validation.
    * The application checks for user errors during inputing of data and provide possible ways to help get or add data.
    ![kologram validation](./assets/images/validate%20input-c.png "view image")
* Project Overview.
    * The application also allows user to view their project status. Including:
        * Date the project was created
        * Name of project
        * Estimated budget created at the start of the project
        * Project due date converted to days countdown
        * Project Outstandings
    ![kologram project overview](./assets/images/project%20overview-c.png "view image")

## Features left to be implemented
Kologram intends to make best use of users' data and provide them with every necessary feature to keep track of their project. such features may include processing of data to better usage. include ways of adding notifications and improve the GUI for users convenience.

## Design
* Google Sheets API
    * The Application uses googlesheets API to keep users data. This makes it possible to view project status at any point in time and keep track of the amount outstanding.
* Pandas Module
    * The Application uses pandas module installed in python to display project overview, and existing projects in a much data-like fashion
* Python Input Command
    * Input questions to collect users data
* Python operations 
    * Calculation of dates to derive number of days left for project
    * Calculation to derive project outstanding amounts
* python print statements 
    * Print statements used to provide useful informatuíons to user
    * Print statement used to structure app pages

## Limitations
* Application is a terminal program and hence, it is limited by these possibity. Applications best behaviour is on a desktop or keyboard type computers.
* Screen size is default to heroku's deployment.

---
# Testing

## Validator testing

## High Level Testing

## Fixed Bugs

## Unfixed Bugs

---
# Deployment

## Project Creation

To start this project, It is recommended to use the [template](https://github.com/Code-Institute-Org/python-essentials-template "Link to Code Institute template") already created by Code Institute. By using this template, necessary plugins for your project are downloaded for you. After clicking this link, the following steps are to be followed.
1. Navigate to "Use this template" on the page.
    * click on the button
1. Navigate to "repostory name"
    * Enter a name for your repository to continue (e.g my-project)
    * You may enter a description for the project. (Not mandatory)
    * keep your repository checked "public" for assessment purposes.
    * Then click on the button "Create repository from template".
1. Are your registered with gitpod by now?
    1. If No ? 
        * Visit the [Gitpod](https://www.gitpod.io "Click to visit gitpod") webiste and Login your details.
        * there after navigate back to Github and continue the steps after login.
    1. If yes ?
        * Navigate to the green button titled **Gitpod**
        * The creation of an environment might take a while. wait for gitpod to set up your environment.
        * It is important to pin your worksheet in Gitpod Dashboard and load subsequent opening of this project from the dashboard in order to keep all installed creds intact.
    1. Here we have Visual Studio code as IDE.
        * By default, on the left side-bar is the respository we created in github including an already made README.md file, package.json, requirements.txt and run.py etc.
            * A mouse right click in this panel area gives us option to create new files and or folders in this repository.
            * Finally, the bash terminal for interacting with github and writing our python code is located right below this window. We can right click on the terminal option to move terminal to right panel
        * To upload changes made in our repository to github in this IDE, the following commands are to be enetered after the $ sign in the bash terminal.
            * To check the status of your repository if any changes have been made.
                 ``` bash
                    git status
            *  To stage changes made 
                ``` bash
                    git add . 
            * To commit changes made 
                ```bash
                    git commit -m "commit message in between this quotes"
            * To push changes made to github
                ```bash
                    git push
            * View files that have been uploaded to github
                ```bash
                    git ls-files
                ```
## Heroku Deployment 

Heroku is the hosting platform for the project and to deploy, The following steps were strictly taken:
[Heroku Address](https://id.heroku.com/ "visit heroku address")
* Sign in to Heroku, otherwise create an account
* From Heroku Dashboard, 
    * click **Create new app**
    * Enter a unique App name
    * create app after selecting region.
* Navigate to settings on Heroku.
    * Navigate to Config Vars
        * in *KEY* enter *CREDS*
        * copy creds.json file, and paste it in *VALUE*, then click on **Add**
        * Add a second *KEY* by inputing *PORT*
        * Enter *8000* as *VALUE*, then click **Add**
    * Navigate to *Add buildpacks* and click on button
        * select first python
        * select second nodejs
* Navigate back to Deploy section
    * Select Github to connect to Github
        * Search for github repository using the name of the repository
        * click connect
    * scroll down to Deploy branch/main
        * Select deploy main to deploy manually. Clicking on this button may take a while
        * After completion, There is a *View* button below it. Click to view live website
[Live website here](https://flo-kologram.herokuapp.com/ "visit live website")

---

# Technologies

* [Python](https://www.python.org/ "Link to Python main-page")
    * Python programming language
* [pandas](https://pandas.pydata.org/ "Link to Pandas main-page")
    * Pandas module, python data analysis module library
* [Google Cloud](https://console.cloud.google.com/ "Link to Google main-page")
    * Google Cloud platform used for the creation of Google drive and Google sheets API linked with the Application
    * Google spreadsheet
    * Google Drive
* [Github](https://github.com "Link to Github main-page")
    * Github is the site used for the commiting and storing of application codes.
* [Heroku Cloud](https://id.heroku.com/ "Link to Heroku login page")
    * Heroku cloud platform is used for the deployment and hosting of program.
* [Gitpod](https://www.gitpod.io "Link to Gitpod main-page")
    * Gitpod is the open-source developer platform used in tandem with github for the deployment of the website source code.
* [Visual Studio code](https://code.visualstudio.com "Link to visual studio code main-page")
    * The Integrated development environment(IDE) used for the writing of source code.
* [TinyJPG](https://tinyjpg.com/ "Link to TinyJPG main-page")
    * Website used for the compression of images used in the website.
* [Techsini](https://techsini.com/multi-mockup/index.php "Link to website main-page")
    * The Mock-up generator website used for creating the website mock-up image.


---
# Credits

## Code
* The turorial from [Code Institute](https://learn.codeinstitute.net/ci_program/diplomainfullstacksoftwarecommoncurriculum "Visit Code Institute") was the most helpful link from the writing of code to the deployment of the program.
* [Edx](https://www.edx.org/ "Link to edx") CS50's Web Programming with Python and JavaScript helpful resource in understanding concepts of javascript.
* Helpful code from  [PyNative](https://pynative.com/python-serialize-datetime-into-json/ "Visit PyNative website") in deciphering Object of type datetime is not JSON serializable.
* Helpful ideas from  [Stack Overflow](https://stackoverflow.com/questions/61180835/typeerror-an-integer-is-required-got-type-tuple-datetime-python "Visit Stack overflow") code for solving TypeError: an integer is required (got type tuple) datetime Python
* Helpful Documentation  [Google Sheet API](https://developers.google.com/ "Visit google sheet API website") to get, update, and append data to and from googlesheets.
* Helpful idea and [Computer Science](https://youtu.be/AnKc74fWYCg "Visit youtube channel") code in creating main page navigation.
* Helpful idea and [Eyehunts](https://tutorial.eyehunts.com/python/convert-list-to-int-python-example-code/#:~:text=Example%20convert%20list%20to%20int%20Python%20Simple%20example,%3D%20int%20%28a_string%29%20print%20%28res%29%20print%20%28type%20%28res%29%29 "Visit Eyehunt code") code in converting list to int.

## Acknowledgement 
My sincere appreciation goes to :
* To my able mentor Ronan, that always come through for me. Thank you always for providing me with relevant tips and information to build these websites.
* To my partner, Mo, for giving her attention at the time of need.