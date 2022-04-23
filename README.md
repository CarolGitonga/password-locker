# Password-Locker

##### By Carol Gitonga

## Table of Content

+ [Description](#description)
+ [User Stories](#user-stories)
+ [Installation Requirement](#Installation)
+ [Behaviour Driven Development](#BDD)
+ [Technology Used](#technology-used)
+ [Licence](#licence)
+ [Authors Info](#author-Info)

## Description
<p>This project is a python application that manages login and sign up credentials of a person for various accounts i.e. username and passwords for each account.</p>

## User Stories
The user would like to.... :
* To create an account for the application or log into the application.
* Store my existing accounts login details for various accounts that i have registered for.
* Generate new password for an account that i haven't registered for and store it with the account name.   
* Delete stored account login details that i do now want anymore.
* Copy my credentials to the clipboard

## Installation

#### The application requires the following installations to operate 
* python3.9
* pyperclip
* pip


### Installation Process
* Open Terminal {Ctrl+Alt+T}

* git clone https://github.com/carol-profile/password-locker.git

* cd password-locker

* code . or atom . based on the text editor you have.


[Go Back to the top](#password-locker)
### Running the Application
* To run the application, open the cloned file in terminal and run the following commands:

        $ chmod +x run.py
        $ ./run.py
* To run test for the application
        $ python3 passlock_test.py

 ## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./run.py```|Hello Welcome to your Accounts Password Store... <br>* CA ---  Create New Account * LI ---  Have An Account |
|Select  CA| input username and password| Hello ```username```, Your account has been created successfully! Your password is: ```password```|
|Select LI  | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a new credential in the application| Enter ```CC```|Enter Account, username, password<br>choose ```tp``` to enter your password or ```gp``` for the application to generate a password for you |
|Display all stored credentials | Enter ```DC```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |
|Find a stored credential based on account name|Enter ```FC```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```D```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exit|
|Exit the application| Enter ```D```| The application exits|

## Technology Used
* python3.9

[Go Back to the top](#password-locker)

## Licence

MIT License

Copyright (c) [2022] [Carol Gitonga]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Go Back to the top](#password-locker)

## Authors Info

Slack Profile - [Carol Gitonga](https://app.slack.com/client/T0101L740P4/D036H8B6WF2/user_profile/U0330AYGJAY)


[Go Back to the top](#password-locker)




