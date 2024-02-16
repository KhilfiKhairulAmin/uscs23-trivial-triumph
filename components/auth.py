"""
Program: auth.py
Author: Trivial Triumph Devs
Provide interface for user authentications in Trivial Triumph
"""


from components.ui import error


def sign_up(new_username: str, new_password: str, repeat_new_password: str, users: dict):
  """
  Register a new user
  """

  # Make sure username is at least 3 characters long and maximum 100 characters long
  if len(new_username) < 3 or len(new_username) > 100:
    error("Username must contain at least 3 characters and maximum of 100 characters")
    return False

  # Make sure username is unique
  if new_username in users.keys():
    error("Username already exists")
    return False

  # Allow underscores
  temp = new_username.replace("_", "")

  # Make sure username only contains alphanumeric characters without space
  if not temp.isalnum():
    error("Username must consists of only alphanumeric characters")
    return False

  # Make sure password is at least 3 characters long and maximum 100 characters long
  if len(new_password) < 3 or len(new_password) > 100:
    error("Password must contain at least 3 characters and maximum of 100 characters")
    return False

  if repeat_new_password != new_password:
    error("Password does not match the repeated password")
    return False

  return True


def log_in(username: str, password: str, users: dict):
  """
  Authenticate existing user
  """
  if username not in users.keys():
    error("Username does not exist")
    return False

  if users[username][0] != password:
    error("Username or password is false")
    return False
  
  return True


if __name__ == "__main__":
  users = {
  # "username": ["password", score1, score2, ..., scoreN],
    "khilfi": ["khilfi", -1],  # Score -1 indicates the player hasn't played the quiz yet
    "yasmin": ["yasmin", 67, 100]
  }
  sign_up(users)
  log_in(users)
