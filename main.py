# import needed procedures, with ["name", "name.py"]
from procedures.wk1.fibonacci import fibo
from procedures.wk1.lists import print_data
from procedures.wk1.lists import for_loop, while_loop, recursive_loop

from procedures.wk0.tree import *
import submenus
from procedures.wk0.tree import christmastree 
from procedures.wk2.lcm import *

main_menu = [
["Lists", "procedures/wk1/lists.py"]]

pat_sub_menu = [
    ["Tree", "procedures/wk0/tree.py"],
    ["Ball", "procedures/wk0/ball.py"],
]
math_sub_menu = [
    ["Matrix", "procedures/wk0/matrix.py"],
    ["Swap", "procedures/wk0/swap.py"],
    ["Fibonacci", "procedures/wk1/fibonacci.py"],
    ["Factorial", "procedures/wk2/factorial.py"],
    ["Lcm", "procedures/wk2/lcm.py"],
    ["Palindrome", "procedures/wk2/palin.py"]
]


# Menu banner is typically defined by menu owner
border = "~" * 25
banner = f"\n{border}\nPlease Select from Menu ☺\n{border}"

# menu blueprint
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Patterns", pat_submenu])
    menu_list.append(["Math", math_submenu])
    buildMenu(title, menu_list)

def pat_submenuc():
  title = "Class Submenu" + banner
  m = submenus.Menu(title, pat_sub_menu)
  m.menu()

def pat_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, pat_sub_menu)

def math_submenuc():
    title = "submenu" + banner
    m = submenus.Menu(title, math_sub_menu)
    m.menu()


def math_submenu():
    title = "submenu" + banner
    buildMenu(title, math_sub_menu)
  
# builds console menu
def buildMenu(banner, options):
    print(banner)
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user input
    choice = input("Type your choice> ")

    # Process user input
    try:
        choice = int(choice)
        if choice == 0:
            # stops
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:
                exec(open(action).read())
            except FileNotFoundError:
                # check main_menu dictionary
                print(f"File not found!: {action}")
    except ValueError:
        # not a number 
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # not one of the numbers listed
        print(f"Invalid choice: {choice}")
  

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()