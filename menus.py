"""
Program: menus.py
Author: Khilfi
Provide all functions for menus
"""


import auth
import db
from ui import display_header, center, error, prompt, prompt_choice, display_header_cinematic


# Global variable storing the username of current user (need log in first)
CurUser = ""

# Global variable containing all user data.
Users = db.get_users_data()


def main_menu():
  """
  Main menu
  """
  # Display header of main menu
  display_header_cinematic()

  # Prompt message
  center("Do you want to register or login?\n")
  center("[1] Register    [2] Login    [3] Quit\n")

  while True:
    try:
      choice = prompt_choice(">", choices=[1, 2, 3])
      
      if choice == 1:
        return 1  # Go to sign up
      elif choice == 2:
        return 2  # Go to login
      elif choice == 3:
        return -1  # Quit the app

    except ValueError as err:
      error(err)
    except KeyboardInterrupt:
      # If user press Ctrl+C, prompt to enter 3 for quitting the app
      print()
      center("Please enter '3' to quit the application.", end="\n\n")


def sign_up_menu():
  """
  Sign up menu
  """
  # Display header of login menu
  display_header()
  center("Sign Up\n")

  while True:
    try:
      username = prompt("Username: ")
      password = prompt("Password: ", hidden=True)
      repeat_password = prompt("Repeat password: ", hidden=True)
      auth.sign_up(username, password, repeat_password, Users)  # Validate the input data for sign up
      # Add the new user
      global Users, CurUser
      Users[username] = [password, -1]
      CurUser = username
      # Save the updated data
      db.save_users_data(Users)
    # Go to home menu
      return 3
    except ValueError as err:
      error(err)
    # If user press Ctrl+C, go back to main menu
    except KeyboardInterrupt:
      return 0  # Go back to main menu


def login_menu():
  """
  Log in menu
  """
  # Display header of login menu
  display_header()
  center("Log In\n")

  while True:
    try:
      username = prompt("Username: ")
      password = prompt("Password: ", hidden=True)
      auth.log_in(username, password, Users)  # Validate the input data for sign up
      # Update the global variables
      global CurUser
      CurUser = username
      # Go to home menu
      return 3
    except ValueError as err:
      error(err)
    except KeyboardInterrupt:
      # If user press Ctrl+C, go back to main menu
      return 0


def home_menu():
  """
  Home menu
  """
  # Display header of home menu
  global CurUser
  display_header(subtitle=f"Welcome {CurUser}!")

  while True:
    pass