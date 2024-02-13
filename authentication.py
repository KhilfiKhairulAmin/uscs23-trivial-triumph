"""
Program: authentication.py
Author: Khilfi
Provide interface for user authentications in Trivial Triumph
"""


def sign_up(new_username: str, new_password: str, repeat_new_password: str, username_list: list[str]):
  """
  Register a new user
  """

  # Make sure username is at least 3 characters long and maximum 100 characters long
  if len(new_username) < 3 or len(new_username) > 100:
    raise ValueError("Username must contain at least 3 characters and maximum of 100 characters")

  # Make sure username is unique
  if new_username in username_list:
    raise ValueError("Username already exists")

  # Allow underscores
  temp = new_username.replace("_", "")

  # Make sure username only contains alphanumeric characters without space
  if not temp.isalnum():
    raise ValueError("Username must consists of only alphanumeric characters")

  # Make sure password is at least 8 characters long and maximum 100 characters long
  if len(new_username) < 8 or len(new_username) > 100:
    raise ValueError("Username must contain at least 8 characters and maximum of 100 characters")

  if repeat_new_password != new_password:
    raise ValueError("Password does not match the repeated password")

  users[new_username] = [new_password, -1]


def log_in(username: str, password: str, username_list: list[str]):
  """
  Authenticate existing user
  """
  if username not in username_list:
    raise ValueError("Username does not exist")

  if users[username][0] != password:
    raise ValueError("Username or password is false")
  
  return True


if __name__ == "__main__":
  users = {
  # "username": ["password", score1, score2, ..., scoreN],
    "khilfi": ["khilfi", -1],  # Score -1 indicates the player hasn't played the quiz yet
    "yasmin": ["yasmin", 67, 100]
  }
  sign_up(users)
  log_in(users)
