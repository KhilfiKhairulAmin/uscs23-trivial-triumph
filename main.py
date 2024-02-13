# TODO Siapkan UI untuk login

import auth
import db
from ui import display_header, center, error, prompt, clear


# Global variable containing all user data.
USERS = db.get_users_data()
"""
Example of how the data looks like:
{
  "username": ["password", 50, 70],
  "khilfi": ["khilfimcg", -1],
  "yasmin": ["yasmin123", 67, 100]
}
"""

# Global variable storing the username of current user
CUR_USER = ""


def main_page():
  """
  Main page
  """
  # Display header of main page
  display_header()
  center("Do you want to register or login?\n")
  center("[1] Register    [2] Login\n")
  
  # Get choice from user
  while True:
    choice = prompt(">", input_width=2)

    # Choice must be integer
    if not choice.isdigit():
      error("Please enter a number\n")
      continue

    # Choice must be between 1 and 2
    choice = int(choice)
    if choice < 1 or choice > 2:
      error("Invalid choice\n")
      continue

    clear()  # Clear terminal screen before going to next page
    if choice == 1: sign_up_page()  # Go to sign up
    elif choice == 2: login_page()  # Go to login
    break


def sign_up_page():
  """
  Sign up page
  """
  # Display header of sign up page
  display_header()
  center("Sign Up\n")

  # Prompt user inputs
  while True:
    try:
      username = prompt("Username: ")
      password = prompt("Password: ")
      repeat_password = prompt("Repeat password: ")
      auth.sign_up(username, password, repeat_password, USERS.keys())  # Validate the input data for sign up
    except ValueError as err:
      error(err)
    else:
      # Add the new user
      USERS[username] = [password, -1]
      CUR_USER = username
      break


def login_page():
  """
  Log in page
  """
  # Display header of login page
  display_header()
  center("Log In\n")
  
  # Prompt user inputs
  while True:
    try:
      username = prompt("Username: ")
      password = prompt("Password: ")
      auth.log_in(username, password, USERS.keys())  # Validate the input data for sign up
    except ValueError as err:
      error(err)
    else:
      # Log in the user
      CUR_USER = username
      break


def home_page():
  display_header()
  print(CUR_USER)
    

def main():
  # Start at main page
  main_page()
  home_page()


if __name__ == "__main__":
  main()
