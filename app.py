# TODO Make home page

import auth
import db
from ui import display_header, center, error, prompt, clear, display_header_cinematic


# Global variable storing the username of current user (need log in first)
CurUser = ""

# Global variable containing all user data.
Users = db.get_users_data()


def main_page():
  """
  Main page
  """
  # Display header of main page
  display_header_cinematic()
  center("Do you want to register or login?\n")
  center("[1] Register    [2] Login    [3] Quit\n")

  while True:
    try:
      choice = prompt(">", input_width=2)

      # Choice must be integer
      if not choice.isdigit():
        raise ValueError("Please enter a number")

      # Choice must be between 1 and 3
      choice = int(choice)
      if choice < 1 or choice > 3:
        raise ValueError("Invalid choice")
      
      if choice == 1:
        return 1  # Go to sign up
      elif choice == 2:
        return 2  # Go to login
      elif choice == 3:
        return -1  # Quit the app

    except ValueError as err:
      error(err)
    # If user press Ctrl+C, prompt to enter 3 for quitting the app
    except KeyboardInterrupt:
      print()
      center("Please enter '3' to quit the application.\n")


def sign_up_page():
  """
  Sign up page
  """
  # Display header of login page
  display_header()
  center("Sign Up\n")

  while True:
    try:
      username = prompt("Username: ")
      password = prompt("Password: ", hidden=True)
      repeat_password = prompt("Repeat password: ", hidden=True)
      auth.sign_up(username, password, repeat_password, Users)  # Validate the input data for sign up

      # Add the new user
      Users[username] = [password, -1]
      # Save the updated data
      db.save_users_data(Users)
    # Go to home page
      return 3
    except ValueError as err:
      error(err)
    # If user press Ctrl+C, go back to main page
    except KeyboardInterrupt:
      return 0  # Go back to main page


def login_page():
  """
  Log in page
  """
  # Display header of login page
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
      # Go to home page
      return 3
    except ValueError as err:
      error(err)
    except KeyboardInterrupt:
      # If user press Ctrl+C, go back to main page
      return 0


def home_page():
  """
  Home page
  """
  # Display header of home page
  display_header(subtitle=f"Welcome {CurUser}!")

  while True:
    pass
    

def main():
  """
  Starting point of the application. This function manages the state of the application throughout its lifecycle.
  """
  State = 0
  while State != -1:
    clear()
    if State == 0:
      State = main_page()
    elif State == 1:
      State = sign_up_page()
    elif State == 2:
      State = login_page()
    elif State == 3:
      State = home_page()


if __name__ == "__main__":
  main()
