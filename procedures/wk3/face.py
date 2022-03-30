import time
import os

# As you can see, its not very optimal 
def smile1():
    print(" _______ ")
    print(" | - - | ")
    print(" |     | ")
    print(" |     | ")
    print(" | \_/ |  ")
    print(" |_____| ")


def smile2():
    print(" _______ ")
    print(" | - - | ")
    print(" |     | ")
    print(" |     | ")
    print(" | ___ |  ")
    print(" |_____| ")

def smile3():
    print(" _______ ")
    print(" | \ / | ")
    print(" |     | ")
    print(" |  _  | ")
    print(" | / \ |  ")
    print(" |_____| ")
  
def main():
  os.system("clear")
  time.sleep(.1)
  smile1()
  time.sleep(.5)
  os.system("clear")
  smile2()
  time.sleep(.5)
  os.system("clear")
  smile3()
  time.sleep(.5)
  os.system("clear")
