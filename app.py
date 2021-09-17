#!/usr/bin/env python3
# -*- coding: utf8 -*-
""""Flask route definitions"""

from flask import Flask # From the flask package import the Flask class

app = Flask(__name__)  # instantiate the Flask class with a parameter __name__ into "app"

@app.route("/") #@app.route is a decorator that wraps the function underneath it.
def index(): # view function that is being wrapped
    return "<h1>Hello, World!</h1>"

# def route(another_function):
    # something potentially happens HERE.
    # then taht other function is called HERE.
    # something else potentially happens HERE.
    # something is returned.

@app.route("/about")
def about_me():
    me = {
        "first_name": "Sarah Jane",
        "last_name": "Villadoz",
        "hobbies": "Play tennis",
        "active": True, true
    }

    # first_name = me["first_name"]
    # first_name = me.get("first_name", "Genie")
        return me