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