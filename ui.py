"""
Program: ui.py
Author: Khilfi
Provide custom functions to display text beautifully in the terminal
"""

WIDTH = 84
ASCII_ART = """

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
  print(text.center(WIDTH), end=end)


def fill(char):
  print(char * WIDTH)


def prompt(prompt_message="", input_width=18) -> str:
  return input(prompt_message.center(WIDTH - input_width).rstrip()+" ")


def display_header():
  print(ASCII_ART)
  center("Welcome to Trivial Triumph!\n")
  fill("*")
  print()


def error(text=""):
  center(f"\033[91m{text}\033[00m")
