"""
Program: menus.py
Author: Trivial Triumph Devs
Provide all functions for menus
"""


import time
import components.auth as auth
import components.db as db
from components.quiz import quizEasy
from components.ui import clear, countdown, display_header, center, fill, good_game, prompt, prompt_choice, display_header_cinematic


MAIN_MENU = 0
SIGN_UP = 1
LOGIN = 2
HOME_MENU = 3
QUIZ = 4
LEADERBOARD = 5
HELP = 6
EXIT = -1


# Global variable storing the username of current user (need log in first)
CurUser = ""

# Global variable containing all user data.
Users: dict[list] = db.get_users_data()


def main_menu():
  """
  Main menu
  """
  try:
    # Display header of main menu
    display_header_cinematic()

    # Prompt message
    center("Do you want to register or login?\n")
    center("[1] Register    [2] Login\n")

    choice = int(prompt_choice(">", choices=[1, 2]))
    
    if choice == 1:
      return SIGN_UP  # Go to sign up
    elif choice == 2:
      return LOGIN  # Go to login
  except KeyboardInterrupt:
    if exit_modal():
      return EXIT  # Quit the application
    return MAIN_MENU


def sign_up_menu():
  """
  Sign up menu
  """
  # Display header of login menu
  display_header()
  center("Sign Up\n")

  global Users, CurUser
  while True:
    username = prompt("Username: ")
    password = prompt("Password: ", hidden=True)
    repeat_password = prompt("Repeat password: ", hidden=True, input_width=24)

    if not auth.sign_up(username, password, repeat_password, Users):  # Validate the input data for sign up
      continue

    # Add the new user
    Users[username] = [password, -1]
    CurUser = username

    # Save the updated data
    db.save_users_data(Users)
    return HOME_MENU  # Go to home menu


def login_menu():
  """
  Log in menu
  """
  # Display header of login menu
  display_header()
  center("Log In\n")

  while True:
    username = prompt("Username: ")
    password = prompt("Password: ", hidden=True)
    if not auth.log_in(username, password, Users):  # Validate the input data for sign up
      continue
    
    # Update the global variables
    global CurUser
    CurUser = username
    return HOME_MENU  # Go to home menu


def home_menu():
  """
  Home menu
  """
  try:
    # Display header of home menu
    global CurUser
    display_header(subtitle=f"Welcome {CurUser}!")

    # Prompt message
    center("Home Menu\n")
    center("(1) Play       ")
    center("(2) Leaderboard")
    center("(3) Help       ")
    center("(4) Logout     ")
    center()

    choice = int(prompt_choice(">", choices=[1, 2, 3, 4]))
    if choice == 1:
      return QUIZ  # Go to quiz menu
    elif choice == 2:
      return LEADERBOARD  # Go to leaderboard menu
    elif choice == 3:
      return HELP  # Go to help menu
    elif choice == 4:
      CurUser = ""  # Reset current user due to logout
      return MAIN_MENU  # Back to main menu
  except KeyboardInterrupt:
    if exit_modal():
      return EXIT  # Quit the application
    return HOME_MENU
  
  
def quiz_menu():
  clear()
  center("Trivial Triumph", col="\033[33m")
  fill("*")
  center()
  center("You will answer 15 fun trivial questions.")
  center("If you answer some of the first 9 questions correctly, you stand a chance on doubling marks in HARD MODE.")
  center("There are MCQ, True/False, Matching, Fill The Blanks, and Subjective questions.", end="\n\n")
  prompt("Press Enter when you're ready!", input_width=0, hidden=True)
  countdown()
  display_header(subtitle="Happy Answering!")
  
  start = time.time()  # Record starting time
  score = quizEasy()  # Run the quiz
  end = time.time()  # Record finishing time

  # Result processing
  time_taken = int(end - start)
  is_new_high_score = score > max(Users[CurUser][1:])

  # Store new score
  if Users[CurUser][1] != -1:
    Users[CurUser].append(score)
  else:
    Users[CurUser][1] = score
  db.save_users_data(Users)

  fill("*")
  center("END OF QUIZ", col="\033[33m")
  time.sleep(1)
  good_game()
  prompt("Press Enter to see result\n", hidden=True, input_width=0)
  fill("*")
  center()
  center("RESULT", col="\033[33m", end="\n\n")
  center(f"Quiz completed!", end="\n\n")
  if is_new_high_score: center(f"NEW PERSONAL HIGH SCORE!", col="\033[32m")
  center(f"Your score is: {score} / 48")
  center(f"Time taken: {time_taken} seconds", end="\n\n")
  fill("*")
  prompt("Back to Home...\n", hidden=True, input_width=0)
  return HOME_MENU  # Go to home menu


def leaderboard_menu():
  pass


def help_menu():
  display_header("")
  center("Controls", end="\n\n")
  center("Navigate       -  [1, 2, 3, 4]      ")
  center("Answer         -  [A..Z, a..z, 0..9]")
  center("Proceed        -  [Enter]           ")
  center("Back/Previous  -  [Ctrl + C]        ")
  center()
  prompt("Back to Home...\n", hidden=True, input_width=1)
  return HOME_MENU  # Go to home menu


def exit_menu():
  clear()


def exit_modal(message="Are you sure you want to quit?"):
  try:
    clear()
    center(message, end="\n\n")
    center("[1] No    [2] Yes")
    center()

    choice = int(prompt_choice(">", choices=[1, 2]))
    if choice == 1:
      return False
    elif choice == 2:
      return True
  except KeyboardInterrupt:
    return False
