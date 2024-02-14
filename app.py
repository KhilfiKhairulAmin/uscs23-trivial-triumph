# TODO Create quiz interface for MCQ,TF
# TODO Test quiz functions for MATCH,SUB,FIB
# TODO Make leaderboard tracker

from components.menus import main_menu, sign_up_menu, login_menu, home_menu, quiz_menu, leaderboard_menu, exit_menu


def main():
  """
  Starting point of the application. This function manages the state of the application.
  """
  state = 0
  while True:
    if state == 0:
      state = main_menu()
    elif state == 1:
      state = sign_up_menu()
    elif state == 2:
      state = login_menu()
    elif state == 3:
      state = home_menu()
    elif state == 4:
      quiz_menu()
    elif state == 5:
      leaderboard_menu()
    elif state == -1:
      exit_menu()
      break


if __name__ == "__main__":
  main()
