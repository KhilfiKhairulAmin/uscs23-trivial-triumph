"""
Program: db.py
Author: Khilfi
Provide interface for database operations in Trivial Triumph
"""

from os import getcwd


# Store current working directory for file reference
CWD = getcwd()

# Path to file where the users data are stored
USER_DATA_FILE = f"{CWD}\data\\users.txt"

# Path to folder containing all questions
QUESTIONS_FOLDER = f"{CWD}\questions"


def get_users_data():
  """
  Read users data from users.txt
  """
  try:
    # Open the database file
    f = open(USER_DATA_FILE, "r")
  except FileNotFoundError:
    # When file is not found, create new file
    new_f = open(USER_DATA_FILE, "w")
    new_f.write("username,password,scores\n")
    new_f.close()
    f = open(USER_DATA_FILE, "r")
  next(f)  # Skip the 1st line, which is the data header (see users.txt file for reference)
  
  users = {}
  # Parse data into dictionary
  for line in f:
    raw = line.strip()
    username, password, *scores = raw.split(",")
    users[username] = [password]
    users[username].extend([int(s) for s in scores])  # Format scores to integer
  return users


def save_users_data(users: dict):
  """
  Write users data into users.txt file
  """
  f = open(USER_DATA_FILE, "w")

  raw = "username,password,scores\n"

  # Parse dictionary data into string
  for username, data in users.items():
    raw += f"{username},{data[0]},{','.join([str(d) for d in data[1:]])}\n"

  f.write(raw)


def load_mcq_questions():
    """
    Read MCQ questions and answers in mcq.txt
    """
    f = open(f"{QUESTIONS_FOLDER}\mcq.txt")

    # Skip the first 6 lines which are the sample questions of the file
    for _ in range(6):
        next(f)  # Skip the line

    mcq = []
    for _ in f:
        question = next(f).strip()
        answers = []
        answers.append(f"A. {next(f).strip()}")
        answers.append(f"B. {next(f).strip()}")
        answers.append(f"C. {next(f).strip()}")
        answers.append(f"D. {next(f).strip()}")
        correct_answer = next(f).strip()
        mcq.append((question, answers, correct_answer))

    return mcq


def load_tf_questions():
    """
    Read True/False questions and answers in tf.txt
    """
    f = open(f"{QUESTIONS_FOLDER}\\tf.txt")

    # Skip the first 2 lines which are the sample questions of the file
    for _ in range(2):
        next(f)  # Skip the line

    tf = []
    for _ in f:
        question = next(f).strip()
        correct_answer = "true" if next(f).strip() == "T" else "false"
        tf.append((question, correct_answer))

    return tf


if __name__ == "__main__":
  save_users_data({'yasmin': ['yasmin', 67, 100], 'khilfi': ['khilfi', -1], 'irfan': ['izerith', -1]})
  get_users_data()
