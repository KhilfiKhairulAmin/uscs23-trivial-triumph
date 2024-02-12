"""
Program: authentication.py
Author: Khilfi
Provide interface for user authentications
"""


def sign_up(users: dict):
  """
  Register a new user
  """

  # Handle username input
  while True:
    new_username = input("Enter a new username: ").strip()

    # Make sure username is at least 3 characters long and maximum 100 characters long
    if len(new_username) < 3 or len(new_username) > 100:
      print("Error: Username must contain at least 3 characters and maximum of 100 characters")
      continue

    # Make sure username is unique
    if new_username in users.keys():
      print("Error: Username already exists")
      continue

    # Allow underscores
    temp = new_username.replace("_", "")

    # Make sure username only contains alphanumeric characters without space
    if not temp.isalnum():
      print("Error: Username must consists of only alphanumeric characters")
      continue

    break

  # Handle password input
  while True:
    new_password = input("Enter a strong password: ")
    repeat_new_password = input("Enter the password again: ")

    if repeat_new_password != new_password:
      print("Error: Password does not match the repeated password")
      continue

    break

  users[new_username] = [new_password, -1]


def log_in(users):
  """
  Authenticate existing user
  """

  while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username not in users.keys():
      print("Username does not exist")
      continue

    if users[username][0] != password:
      print("Password is invalid")
      continue  

    break


if __name__ == "__main__":
  users = {
  # "username": ["password", score1, score2, ..., scoreN],
    "khilfi": ["khilfi", -1],  # Score -1 indicates the player hasn't played the quiz yet
    "yasmin": ["yasmin", 67, 100]
  }
  sign_up(users)
  log_in(users)
