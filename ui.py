"""
Program: ui.py
Author: Khilfi
Provide custom functions to display text beautifully in the terminal
"""

# Width of the terminal
WIDTH = 84

# Source: https://patorjk.com/software/taag/#p=display&v=2&f=Delta%20Corps%20Priest%201&t=TRIVIAL%0ATRIUMPH
TRIVIAL_TRIUMPH_ASCII_ART = """

           ███        ▄████████  ▄█   ▄█    █▄   ▄█     ▄████████  ▄█                       
       ▀█████████▄   ███    ███ ███  ███    ███ ███    ███    ███ ███                       
          ▀███▀▀██   ███    ███ ███▌ ███    ███ ███▌   ███    ███ ███                       
           ███   ▀  ▄███▄▄▄▄██▀ ███▌ ███    ███ ███▌   ███    ███ ███                       
           ███     ▀▀███▀▀▀▀▀   ███▌ ███    ███ ███▌ ▀███████████ ███                       
           ███     ▀███████████ ███  ███    ███ ███    ███    ███ ███                       
           ███       ███    ███ ███  ███    ███ ███    ███    ███ ███▌    ▄                 
          ▄████▀     ███    ███ █▀    ▀██████▀  █▀     ███    █▀  █████▄▄██                 
                     ███    ███                                   ▀             

    ███        ▄████████  ▄█  ███    █▄    ▄▄▄▄███▄▄▄▄      ▄███████▄    ▄█    █▄    
▀█████████▄   ███    ███ ███  ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███   
   ▀███▀▀██   ███    ███ ███▌ ███    ███ ███   ███   ███   ███    ███   ███    ███   
    ███   ▀  ▄███▄▄▄▄██▀ ███▌ ███    ███ ███   ███   ███   ███    ███  ▄███▄▄▄▄███▄▄ 
    ███     ▀▀███▀▀▀▀▀   ███▌ ███    ███ ███   ███   ███ ▀█████████▀  ▀▀███▀▀▀▀███▀  
    ███     ▀███████████ ███  ███    ███ ███   ███   ███   ███          ███    ███   
    ███       ███    ███ ███  ███    ███ ███   ███   ███   ███          ███    ███   
   ▄████▀     ███    ███ █▀   ████████▀   ▀█   ███   █▀   ▄████▀        ███    █▀    
              ███    ███                                                             

"""


def center(text="", end="\n"):
  """
  Print text on the center of the terminal
  """
  print(text.center(WIDTH), end=end)


def fill(char):
  """
  Fill the line with the character
  """
  print(char * WIDTH)


def prompt(prompt_message="", input_width=18) -> str:
  """
  Prompt user input at the center of the terminal
  """
  return input(prompt_message.center(WIDTH - input_width).rstrip()+" ")


def display_header():
  """
  Display Trivial Triumph remarkable header
  """
  print(TRIVIAL_TRIUMPH_ASCII_ART)
  center("Welcome to Trivial Triumph!\n")
  fill("*")
  print()


def error(text=""):
  """
  Print error message in red colour
  """
  center(f"\033[91m{text}\033[00m\n")
