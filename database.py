"""
Program: database.py
Author: Khilfi
Provide interface for database operations
"""

def load_data():
  f = open("users.txt", "r")
  next(f)  # Skip the 1st line, which is the data header (see users.txt file for reference)
  
  users = {}
  for line in f:
    raw = line.strip()
    username, password, *scores = raw.split(",")
    users[username] = [password]
    users[username].extend([int(s) for s in scores])

  return users


def save_data(users: dict):
  f = open("users.txt", "w")

  raw = "username,password,scores\n"
  for username, data in users.items():
    raw += f"{username},{data[0]},{','.join([str(d) for d in data[1:]])}\n"

  f.write(raw)


if __name__ == "__main__":
  save_data({'yasmin': ['yasmin', 67, 100], 'khilfi': ['khilfi', -1], 'irfan': ['izerith', -1]})
  load_data()
