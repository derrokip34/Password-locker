#!/usr/bin/env python3.6
from password import User
from password import Credentials

def create_login(fname,lname,password):
    """
    function to create a new User
    """
    new_user = User(fname,lname,password)
    return new_user

def add_account(accname,username,accpassword):
    """
    function to create a new account
    """
    new_credentials = Credentials(accname,username,accpassword)
    return new_credentials

def save_user(user):
    """
    function to save user
    """
    user.save_user()

def save_credentials(account):
    """
    function to save credentials
    """
    account.save_credentials()

def generate_password():
    """
    function to generate a password
    """
    password = Credentials.generate_password()
    return password

def display_credentials():
    """
    function to display account credentials
    """
    return Credentials.display_credentials()

def delete_account(credential):
    """
    function to delete an account
    """
    return credential.delete_credentials()

