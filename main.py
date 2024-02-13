# TODO Siapkan UI untuk login

import authentication as auth
import database as db
from ui import *


def main_page():
  # Display header of main page
  display_header()
  center("Do you want to register or login?\n")
  center("[1] Register    [2] Login\n")
  
  # Get choice from user
  while True:
    try:
      choice = prompt(">", input_width=2)

      # Choice must be integer
      if not choice.isdigit():
        raise ValueError("Please enter a number\n")

      # Choice must be between 1 and 2
      if choice < 1 or choice > 2:
        raise ValueError("Invalid choice\n")

      choice = int(choice)
      if choice == 1:
        sign_up_page()  # Go to sign up
      elif choice == 2:
        login_page()  # Go to login

    except ValueError as err:
      error(err)
    else:
      break


def login_page():
  print(TRIVIAL_TRIUMPH_ASCII_ART)
  center("Welcome to Trivial Triumph!\n")
  fill("*")
  print()
  center("Log In\n")
  username = prompt("Username: ")
  password = prompt("Password: ")


def sign_up_page():
  # Display header of sign up page
  display_header()
  center("Sign Up\n")

  # Prompt user inputs
  while True:
    try:
      username = prompt("Username: ")
      password = prompt("Password: ")
      repeat_password = prompt("Repeat password: ")
      auth.sign_up(username, password, repeat_password, users.keys())
    except ValueError as err:
      error(err)
    else:
      break
    

def main():
  # Global variable containing all user data
  global users
  users = db.get_users_data()

  # Start at main page
  main_page()


if __name__ == "__main__":
  main()
