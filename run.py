#!/usr/bin/env python3.6
from password import User
from password import Credentials
import getpass

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

def find_credential(account_name):
    """
    function that finds a credential by account_name
    """
    return Credentials.find_by_name(account_name)

def main():
    print("""
    Welcome. Use these short codes:
    ca: create a new Password locker account
    ex: exit the application
          """)
    while True:
        short_code = input().lower()
        if short_code == 'ca':
            print("Enter your first name")
            fname = input()

            print("Enter your last name")
            lname = input()

            print("Do you want an auto-generated password ? yes or no")
            answer = input()
            if answer == 'no':
                print("Enter you password")
                password = input()
            else:
                password = generate_password()
                print(f"Your generated password is {password}")

            save_user(create_login(fname,lname,password))
            print('\n')

            while True:
                print("""
                Welcome .Use the following commands:
                acc: create a new account
                daa: display all accounts
                dac: delete an account
                lg: log out
                """)
                print('\n')
                shrt_code = input().lower()

                if shrt_code == 'acc':
                    print("Enter name of new account")
                    accname = input()

                    print("Enter your username for this account")
                    username = input()
                    
                    print("Type in your account password")
                    accpass = input()

                    save_credentials(add_account(accname,username,accpass))
                    print('\n')
                    print("Your new account has been created")

                elif shrt_code =='daa':
                    if display_credentials():
                        for credential in display_credentials():
                            print("Here are your accounts")
                            print('\n')
                            print(f"Account name =>{credential.account_name} \n Account username =>{credential.username}")
                            print('='*20)

                elif shrt_code == 'dac':
                    print("Enter account name to delete")
                    accdel = input()
                    acc_del = find_credential(accdel)
                    delete_account(acc_del)
                    print(f"{accdel} has been deleted")

                elif shrt_code == 'lg':
                    print("Thank for using this app")
                    break
                else:
                    print("This command does not exist")
                    print('='*8)

        elif short_code == 'ex':
            print("Hope you enjoyed using the application")
            break

        else:
            print('\n')
            print("Sorry the command does not exist. Try again")

if __name__ == '__main__':
    main()