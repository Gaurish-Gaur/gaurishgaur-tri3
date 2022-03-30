# import needed procedures, with ["name", "name.py"]
import procedures.wk0.ball
import procedures.wk0.tree
import procedures.wk1.lists
import procedures.wk0.matrix
import procedures.wk0.swap
import procedures.wk1.fibonacci
import procedures.wk3.face
import procedures.wk3.rps
import procedures.wk2.factorial
import procedures.wk2.lcm
import procedures.wk2.palin

from time import sleep
import sys

welcome = "Welcome to Gaur's Menu"

def hi():
  for x in welcome:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.1)

main_menu = [
["Lists", procedures.wk1.lists.tester]]

pat_sub_menu = [
    ["Tree", procedures.wk0.tree.main],
    ["Ball", procedures.wk0.ball.main],
    ["Face", procedures.wk3.face.main],
    ["Rock Paper Scissors", procedures.wk3.rps.play],
]
math_sub_menu = [
    ["Matrix", procedures.wk0.matrix.main],
    ["Swap", procedures.wk0.swap.main],
    ["Fibonacci", procedures.wk1.fibonacci.tester],
    ["Factorial", procedures.wk2.factorial.main],
    ["Lcm", procedures.wk2.lcm.tester],
    ["Palindrome", procedures.wk2.palin.main]
]


# Menu banner is typically defined by menu owner
border = "~" * 25
banner = f"\n{border}\nPlease Select from Menu ☺\n{border}"

# menu blueprint
def menu():
    title = ":)" + banner
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
    hi()
    menu()