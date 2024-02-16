# TODO 15/5/2024
# TODO Make leaderboard tracker (YASMIN)

# TODO 16/4/2024
# TODO Integrate Leaderboard menu

# TODO Sometime later...
# TODO Small Report about quiz app
# TODO Update README file

from components.menus import STATISTIC, exit_menu, help_menu, main_menu, player_statistics_menu, sign_up_menu, login_menu, home_menu, quiz_menu, leaderboard_menu, \
                             MAIN_MENU, SIGN_UP, LOGIN, HOME_MENU, QUIZ, LEADERBOARD, HELP, EXIT


def main():
  """
  Starting point of the application. This function manages the state of the application.
  """
  prev_menu = -1
  cur_menu = 0

  while True:
    try:
        if cur_menu == MAIN_MENU:
          cur_menu = main_menu()  # Parent menu 1
        
        elif cur_menu == SIGN_UP:
          prev_menu = MAIN_MENU
          cur_menu = sign_up_menu()
        
        elif cur_menu == LOGIN:
          prev_menu = MAIN_MENU
          cur_menu = login_menu()

        elif cur_menu == HOME_MENU:
          cur_menu = home_menu()  # Parent menu 2

        elif cur_menu == QUIZ:
          prev_menu = HOME_MENU
          cur_menu = quiz_menu()

        elif cur_menu == LEADERBOARD:
          prev_menu = HOME_MENU
          cur_menu = leaderboard_menu()

        elif cur_menu == STATISTIC:
          prev_menu = HOME_MENU
          cur_menu = player_statistics_menu()

        elif cur_menu == HELP:
          prev_menu = HOME_MENU
          cur_menu = help_menu()

        elif cur_menu == EXIT:
          exit_menu()
          break

    # If user press Ctrl+C, go back to previous menu
    except KeyboardInterrupt:
      cur_menu = prev_menu


if __name__ == "__main__":
  main()
