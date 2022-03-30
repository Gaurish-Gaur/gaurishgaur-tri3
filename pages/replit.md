{% include replits.html %}

# Week 0 - Animations

### Code for Ball Animation

```
import time
import os

# As you can see, its not very optimal 
def frame1():
    print("()      ")
    print("      ")
    print("      ")
    print("------------")


def frame2():
    print("      ")
    print(" ()   ")
    print("      ")
    print("------------")


def frame3():
    print("          ")
    print("         ")
    print("   ()     ")
    print("------------")


def frame4():
    print("         ")
    print("         ")
    print("         ")
    print("-----()------")


def frame5():
    print("          ")
    print("          ")
    print("       ()   ")
    print("------------")


def frame6():
    print("            ")
    print("           ()")
    print("          ")
    print("------------")


def frame7():
    print("               () ")
    print("            ")
    print("            ")
    print("------------")

def main():
  os.system("clear")
  time.sleep(.1)
  frame1()
  time.sleep(.5)
  os.system("clear")
  frame2()
  time.sleep(.5)
  os.system("clear")
  frame3()
  time.sleep(.5)
  os.system("clear")
  frame4()
  time.sleep(.5)
  os.system("clear")
  frame5()
  time.sleep(.5)
  os.system("clear")
  frame6()
  time.sleep(.5)
  os.system("clear")
  frame7()
  time.sleep(.5)
  os.system("clear")
  print("Yay!")
  time.sleep(.5)
  os.system("clr")
```
# Week 1 - Lists and Loops

### Code for Lists

```
InfoDb.append({  
               "FirstName": "Gaurish",  
               "LastName": "Gaur",  
               "Balance": "10",  
               "Email": "gaurishgaur3@gmail.com",   
               "Fav_Restraunts":["Chipolte","Pizza Hut","Subway"] , 
               "Least_Fav_Restraunts":["Rubios", "Round Table"]
              })  

InfoDb.append({  
               "FirstName": "Saurav",  
               "LastName": "Nagpal",  
               "Balance": "100",  
               "Email": "sauravnagpal0@gmail.com ",  
               "Fav_Restraunts":["Dominos","McDonalds", "Jamba Juice"],
                "Least_Fav_Restraunts":["Wendys", "Gorgai"]

              })  
InfoDb.append({  
               "FirstName": "Aniruff",  
               "LastName": "Ramachandran",  
               "Balance": "37",  
               "Email": "aramachandran1012@gmail.com",  
               "Fav_Restraunts":["Chick-fil-A", "Gorgai", "Board and Brew"],
               "Least_Fav_Restraunts":["Daphnies", "Jack-in-the-box"]
              })  
```
### Code for Loops

```

def print_data(n):
    print(InfoDb[n]["LastName"], InfoDb[n]["Balance"], InfoDb[n]["Email"])  # using comma puts space between values
    print("\t", "Favorite Restraunts: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Fav_Restraunts"]))  # join allows printing a string list with separator
    print()

  
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return 


```

### Code for Fibonacci

```
def fibo(n):
	if n <= 0:
		return [0]
	s = [0,1]
	while len(s) < n:
		hold = len(s)
		rec = s[hold - 1] + s[hold - 2]
		s.append(rec)
	return s
```

# Week 2 - Math

### Code for Factorial
```
class F:
  def __call__(self, num):
    final = 1 #for zero or one
    for i in range(1, num + 1): #range is non exclusive, needs to stop at num, not at right before num
      final *= i
    return final
def main():
  factorial = F()
  number = input("Factorial for: ")
  number = int(number)
  print("The factorial of ", number, "is",   factorial(number))
```

### Code for LCM
```
def findlcm(a, b):
    if (a > b):
        maximum = a
    else:
        maximum = b
    while (True):
        if (maximum % a == 0 and maximum % b == 0):
            break
        maximum = maximum + 1
    return maximum

class Lcm:
  def __init__(self, a, b):
    self.a = a
    self.b = b
  
  def __call__(self):
    if self.a > self.b:
      s = self.b

    if self.b > self.a:
      s = self.a  
      
    while (True):
      if (s % self.a == 0 and s % self.b == 0):
        break
      s = s + 1
    return s

def tester():
	num = input("Imperative [I] or OOP [O]")
	try:
		if num == 'I':
			print("The LCM, Least Common Multiple, of 9 and 12 is : ",end="")
			print(findlcm(9,12))
		elif num == 'O':
			L = Lcm(9,12)
			print("The LCM, Least Common Multiple, of 9 and 12 is : ",end="")
			print(L())
	except:
		print("Sorry, try again!")
```

### Code for Palindrome
```
def main():
  list = ["kayak", "Aniruff", "racecar", "r%ace /!@# ca%r", "H!ey!@#"]
  reflection = ""
  badchar = " !@#$%^&*()/~|"
  
  for examples in list:
    print("Input:", examples)
    
    for char in badchar:
      examples = examples.replace(char, "")
      cleanexamples = examples.replace(char, "")
      examples = examples.lower()
      reflection = examples[::-1] 
    print("Input(purified):", cleanexamples) 
    print("Output:", examples)  
    
    if (examples == reflection):
      print(examples, "IS a palindrome \n")
    else:
      print(examples, "IS NOT a palindrome \n")
```

