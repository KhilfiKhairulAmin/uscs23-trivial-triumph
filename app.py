# TODO 15/5/2024
# TODO Make leaderboard tracker (YASMIN)

# TODO 16/4/2024
# TODO Quit menu
# TODO Integrate Leaderboard menu

# TODO Sometime later...
# TODO Small Report about quiz app
# TODO Update README file

from components.menus import help_menu, main_menu, sign_up_menu, login_menu, home_menu, quiz_menu, leaderboard_menu, exit_menu


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
      state = quiz_menu()
    elif state == 5:
      leaderboard_menu()
    elif state == 6:
      state = help_menu()
    elif state == -1:
      exit_menu()
      break


if __name__ == "__main__":
  main()
