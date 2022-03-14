# import needed procedures, with ["name", "name.py"]
import submenus
main_menu = [
    ["matrix", "procedures/matrix.py"],
    ["swap", "procedures/swap.py"],
]

sub_menu = [
    ["tree", "procedures/tree.py"],
    ["ball", "procedures/ball.py"],
]


# Menu banner is typically defined by menu owner
border = "~" * 25
banner = f"\n{border}\nPlease Select from Menu ☺\n{border}"

# menu blueprint
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Patterns", submenu])
    buildMenu(title, menu_list)

def submenuc():
  title = "Class Submenu" + banner
  m = submenus.Menu(title, sub_menu)
  m.menu()

def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)

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