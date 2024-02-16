# TODO 15/5/2024
# TODO Make leaderboard tracker (YASMIN)

# TODO 16/4/2024
# TODO Handle KeyboardInterrupt during quiz
# TODO Improve UI for quit modal
# TODO Implement exit menu display
# TODO Integrate Leaderboard menu

# TODO Sometime later...
# TODO Small Report about quiz app
# TODO Update README file

from components.menus import exit_menu, help_menu, main_menu, sign_up_menu, login_menu, home_menu, quiz_menu, leaderboard_menu, exit_modal


def main():
  """
  Starting point of the application. This function manages the state of the application.
  """
  prev_menu = -1
  cur_menu = 0

  while True:
    try:
        if cur_menu == 0:
          cur_menu = main_menu()  # Parent menu 1
        elif cur_menu == 1:
          prev_menu = 0
          cur_menu = sign_up_menu()
        elif cur_menu == 2:
          prev_menu = 0
          cur_menu = login_menu()
        elif cur_menu == 3:
          cur_menu = home_menu()  # Parent menu 2
        elif cur_menu == 4:
          prev_menu = 3
          cur_menu = quiz_menu()
        elif cur_menu == 5:
          prev_menu = 3
          leaderboard_menu()
        elif cur_menu == 6:
          prev_menu = 3
          cur_menu = help_menu()
        elif cur_menu == -1:
          exit_menu()
          break

    # If user press Ctrl+C, go back to previous menu
    except KeyboardInterrupt:
      cur_menu = prev_menu


if __name__ == "__main__":
  main()
