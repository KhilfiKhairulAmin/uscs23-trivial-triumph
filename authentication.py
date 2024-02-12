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
    temp = new_username
    if "_" in new_username:
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

    if repeat_new_password == new_password:
      print("Error: Password does not match the repeated password", "\n")
      continue

    break

  users[new_username] = [new_password, -1]


def log_in(existing_users):
  pass


if __name__ == "__main__":
  sign_up(["khilfi", "yasmin"])
  # log_in()
