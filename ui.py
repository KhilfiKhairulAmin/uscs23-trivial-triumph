"""
Program: ui.py
Author: Khilfi
Provide custom functions to display text beautifully in the terminal
"""

from time import sleep
import os

# Width of the terminal
WIDTH = 84

# Source: https://patorjk.com/software/taag/#p=display&v=2&f=Delta%20Corps%20Priest%201&t=TRIVIAL%0ATRIUMPH
TRIVIAL_ASCII_ART = """
           ███        ▄████████  ▄█   ▄█    █▄   ▄█     ▄████████  ▄█                       
       ▀█████████▄   ███    ███ ███  ███    ███ ███    ███    ███ ███                       
          ▀███▀▀██   ███    ███ ███▌ ███    ███ ███▌   ███    ███ ███                       
           ███   ▀  ▄███▄▄▄▄██▀ ███▌ ███    ███ ███▌   ███    ███ ███                       
           ███     ▀▀███▀▀▀▀▀   ███▌ ███    ███ ███▌ ▀███████████ ███                       
           ███     ▀███████████ ███  ███    ███ ███    ███    ███ ███                       
           ███       ███    ███ ███  ███    ███ ███    ███    ███ ███▌    ▄                 
          ▄████▀     ███    ███ █▀    ▀██████▀  █▀     ███    █▀  █████▄▄██                 
                     ███    ███                                   ▀             
"""
TRIUMPH_ASCII_ART = """
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
TRIVIAL_TRIUMPH_ASCII_ART = TRIVIAL_ASCII_ART + TRIUMPH_ASCII_ART

def clear():
  """
  Clear the terminal
  """
  os.system("clear")
  os.system("cls")


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


def display_header(subtitle="Welcome to Trivial Triumph!"):
  """
  Display Trivial Triumph remarkable header
  """
  print(TRIVIAL_TRIUMPH_ASCII_ART)
  center(f"{subtitle}\n")
  fill("*")
  print()


def display_header_cinematic(subtitle="Welcome to Trivial Triumph!"):
  """
  Display Trivial Triumph remarkable header cinematically
  """
  sleep(1)
  print(TRIVIAL_ASCII_ART, end="")
  sleep(1.5)
  print(TRIUMPH_ASCII_ART)
  sleep(1.5)
  center(f"{subtitle}\n")
  sleep(2)
  fill("*")
  print()


def error(text=""):
  """
  Print error message in red colour
  """
  center(f"\033[91m{text}\033[00m\n")
