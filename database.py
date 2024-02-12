"""
Program: database.py
Author: Khilfi
Provide interface for database operations in Trivial Triumph
"""

def load_data():
  """
  Read users data from users.txt
  """
  f = open("users.txt", "r")
  next(f)  # Skip the 1st line, which is the data header (see users.txt file for reference)
  
  users = {}

  # Parse data into dictionary
  for line in f:
    raw = line.strip()
    username, password, *scores = raw.split(",")
    users[username] = [password]
    users[username].extend([int(s) for s in scores])  # Format scores to integer

  return users


def save_data(users: dict):
  """
  Write users data into users.txt file
  """
  f = open("users.txt", "w")

  raw = "username,password,scores\n"

  # Parse dictionary data into string
  for username, data in users.items():
    raw += f"{username},{data[0]},{','.join([str(d) for d in data[1:]])}\n"

  f.write(raw)


if __name__ == "__main__":
  save_data({'yasmin': ['yasmin', 67, 100], 'khilfi': ['khilfi', -1], 'irfan': ['izerith', -1]})
  load_data()
