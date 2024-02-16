"""
Program: menus.py
Author: Trivial Triumph Devs
Provide all functions for menus
"""


import time
import components.auth as auth
import components.db as db
from components.quiz import quizEasy
from components.ui import clear, countdown, display_header, center, error, fill, good_game, prompt, prompt_choice, display_header_cinematic


# Global variable storing the username of current user (need log in first)
CurUser = ""

# Global variable containing all user data.
Users: dict[list] = db.get_users_data()


def main_menu():
  """
  Main menu
  """
  # Display header of main menu
  display_header_cinematic()

  # Prompt message
  center("Do you want to register or login?\n")
  center("[1] Register    [2] Login    [3] Quit\n")

  while True:
    try:
      choice = int(prompt_choice(">", choices=[1, 2]))
      
      if choice == 1:
        return 1  # Go to sign up
      elif choice == 2:
        return 2  # Go to login

    except ValueError as err:
      error(err)
    except KeyboardInterrupt:
      # If user press Ctrl+C, prompt to enter 3 for quitting the app
      exit_modal()


def sign_up_menu():
  """
  Sign up menu
  """
  # Display header of login menu
  display_header()
  center("Sign Up\n")

  global Users, CurUser
  while True:
    try:
      username = prompt("Username: ")
      password = prompt("Password: ", hidden=True)
      repeat_password = prompt("Repeat password: ", hidden=True, input_width=24)
      auth.sign_up(username, password, repeat_password, Users)  # Validate the input data for sign up
      # Add the new user
      Users[username] = [password, -1]
      CurUser = username
      # Save the updated data
      db.save_users_data(Users)
    # Go to home menu
      return 3
    except ValueError as err:
      error(err)
    # If user press Ctrl+C, go back to main menu
    except KeyboardInterrupt:
      return 0  # Go back to main menu


def login_menu():
  """
  Log in menu
  """
  # Display header of login menu
  display_header()
  center("Log In\n")

  while True:
    try:
      username = prompt("Username: ")
      password = prompt("Password: ", hidden=True)
      auth.log_in(username, password, Users)  # Validate the input data for sign up
      # Update the global variables
      global CurUser
      CurUser = username
      # Go to home menu
      return 3
    except ValueError as err:
      error(err)
    except KeyboardInterrupt:
      # If user press Ctrl+C, go back to main menu
      return 0


def home_menu():
  """
  Home menu
  """
  # Display header of home menu
  global CurUser
  display_header(subtitle=f"Welcome {CurUser}!")

  while True:
    try:
      # Prompt message
      center("Home Menu\n")
      center("(1) Play       ")
      center("(2) Leaderboard")
      center("(3) Help       ")
      center("(4) Logout     ")
      center()
      choice = int(prompt_choice(">", choices=[1, 2, 3, 4]))

      if choice == 1:
        return 4  # Go to quiz menu
      elif choice == 2:
        return 5  # Go to leaderboard menu
      elif choice == 3:
        return 6  # Go to help menu
      elif choice == 4:
        CurUser = ""  # Reset current user due to logout
        return 0  # Back to main menu
    except ValueError as err:
      error(err)
    except KeyboardInterrupt:
      exit_modal()
    
  
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
  return 3  # Go to home menu


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
  return 3  # Go to home menu


def exit_modal(message="Are you sure you want to quit?"):
  center(message, end="\n\n")
  center("[1] No    [2] Yes")
  center()

  while True:
    try:
      choice = int(prompt_choice(">", choices=[1, 2]))
      
      if choice == 1:
        return
      elif choice == 2:
        exit()

    except ValueError as err:
      error(err)
    except KeyboardInterrupt:
      # If user press Ctrl+C, prompt to enter 3 for quitting the app
      return
