# TODO Make home menu

from menus import main_menu, sign_up_menu, login_menu, home_menu


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
    elif state == -1:
      break


if __name__ == "__main__":
  main()
