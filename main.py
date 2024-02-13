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

    if choice < 1 or choice > 2:
      error("Invalid choice\n")
      continue

    return choice


def login_page():
  print(ASCII_ART)
  center("Welcome to Trivial Triumph!\n")
  fill("*")
  print()
  center("Log In\n")
  username = prompt("Username: ")
  password = prompt("Password: ")


def sign_up_page():
  pass


def main():
  state = main_page()



if __name__ == "__main__":
  main()
