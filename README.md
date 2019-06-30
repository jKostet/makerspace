# Page for Kumpula Think Company Makerspace (+ python tsoha19)

Heroku @ https://kumpulamakerspace.herokuapp.com/

Test User for TSOHA,

	username: hello

	password: world

## Makerspace Wish List (+ Future Inventory & Updates page)
The application works as a Wish List for the Makerspace. The users of the Makerspace can wish-list equipment they would like.

The plan is to later add an inventory and updates, so users can browse a list of equipment, parts, tools and services available at the Makerspace, and  Administrators of the Makerspace can manage the inventory and post updates on Makerspace development, such as new equipment being available, maintenance notices or upcoming events.


Functions:
* Registration and Login for users
* Browsing equipment Wish List
* Approving Wishes/Requests (Admins)
* Adding items to Wish List


Potential future additions:
* Marking Wishes as fulfilled
* Browsing Inventory
* Managing Inventory (add, remove, update description)
* Posting updates to front page


## Documentation
* [Use cases](https://github.com/jKostet/makerspace/blob/master/documentation/doc.md)
* [Database Graph](https://github.com/jKostet/makerspace/blob/master/documentation/db.png)

# Setup and Install

## Setup Python Virtual Environment
`apt-get install python3-pip`

`pip3 install virtualenv`

`python3 -m venv venv`

`source venv/bin/activate`

## Installing required libs
`pip install -r requirements.txt`

# Start server
`python run.py`

# Create admin account
Open the app in browser, and register a new account with username `admin`, you'll be granted admin rights.

# Deploying to heroku
Create a Heroku account, install Heroku CLI and clone the repo.
`heroku login`

`heroku apps:create APPNAME/URL`

`git push heroku master`
