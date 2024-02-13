# TODO Make state machine for this app
# TODO Make handler for going back to previous state
# TODO Make home page

import auth
import db
from ui import display_header, center, error, prompt, clear, display_header_cinematic


# Global variable storing the username of current user (need log in first)
CUR_USER = ""

# Global variable containing all user data.
USERS = db.get_users_data()

# Global variable that store the current state of the application


def main_page():
  """
  Main page
  """
  # Display header of main page
  clear()
  display_header_cinematic()
  center("Do you want to register or login?\n")
  center("[1] Register    [2] Login\n")
  
  # Get choice from user
  while True:
    choice = prompt(">", input_width=2)

    # Choice must be integer
    if not choice.isdigit():
      error("Please enter a number")
      continue

    # Choice must be between 1 and 2
    choice = int(choice)
    if choice < 1 or choice > 2:
      error("Invalid choice")
      continue

    clear()  # Clear terminal screen before going to next page
    if choice == 1: sign_up_page()  # Go to sign up
    elif choice == 2: login_page()  # Go to login
    clear()
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
      password = prompt("Password: ", hidden=True)
      repeat_password = prompt("Repeat password: ", hidden=True)
      auth.sign_up(username, password, repeat_password, USERS)  # Validate the input data for sign up
    except ValueError as err:
      error(err)
    else:
      # Add the new user and save
      USERS[username] = [password, -1]
      db.save_users_data(USERS)

      global CUR_USER
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
      password = prompt("Password: ", hidden=True)
      auth.log_in(username, password, USERS)  # Validate the input data for sign up
    except ValueError as err:
      error(err)
    else:
      # Log in the user
      global CUR_USER
      CUR_USER = username
      break


def home_page():
  global CUR_USER
  display_header(subtitle=f"Welcome {CUR_USER}!")
    

def main():
  # Start at main page
  main_page()
  home_page()


if __name__ == "__main__":
  main()
