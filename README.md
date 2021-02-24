# Coffeeshop - fullstack project

This is a full stack drink menu application for Udacity students.

If you're a student, you can look at what's on the menue. If you're a barista, you can look at  the details of those drinks. If you're a manager, you can basicly do whatever you want.

You can add drinks, edit them, update them, and even delete them if you find them not selling well enough.

# How to install

The stack contains 2 parts, frontend and backend. Lets start with the backend first.

## backend

First things first, you need python. Download it from [here](https://www.python.org/downloads/)

Then, Move to the backend folder and then install the requirements.txt file like this:

pip install -r requirements.txt

Then, type "set FLASK_APP=api.py"
Then type "flask run"

Now that we got our flask server running, lets move to the frontend side of things.

## frontend

The frontend depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

You also need the Ionic Command Line Interface to build it. You can find more info [here](https://ionicframework.com/docs/installation/cli)

Now that's done, you need to move to the frontend folder and type "npm install".
Then type "ionic serve".

In a few seconds the server will start and a web  page will open on your browser, and you can enjoy the app.

# Note

In order for you to get the authorization part working, you need to do a few more steps:

You need to sign up for [an auth0 account](https://auth0.com)

Please take a look at the README file that's in the backend folder for more information on what to do next.