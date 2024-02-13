# TODO Siapkan UI untuk login

import authentication as auth
import database as db
from ui import *


def main_page():
  display_header()
  center("Do you want to register or login?\n")
  center("[1] Register    [2] Login\n")
  
  while True:
    choice = prompt("=>", input_width=2)

    if not choice.isdigit():
      error("Please enter a number\n")
      continue

    choice = int(choice)

    if choice == 1:
      sign_up_page()
      break
    elif choice == 2:
      login_page()
      break
    else:
      error("Invalid choice\n")
      continue


def login_page():
  print(ASCII_ART)
  center("Welcome to Trivial Triumph!\n")
  fill("*")
  print()
  center("Log In\n")
  username = prompt("Username: ")
  password = prompt("Password: ")


def sign_up_page():
  display_header()
  center("Sign Up\n")
  username = prompt("Username: ")
  password = prompt("Password: ")
  repeat_password = prompt("Repeat password: ")
  auth.sign_up(username, password, repeat_password, users.keys())
  pass


def main():
  # Global variable containing all user data
  global users
  users = db.get_users_data()


if __name__ == "__main__":
  main()
