InfoDb = []
# List with dictionary records placed in a list  
#List includes many indicators, like FirstName or Balance. Balance could mean amount of credu one had and is ready to spend. As in, do they have the balance to spend at perhaps a more expensive restraunt?
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
InfoDb.append({  
               "FirstName": "Connor",  
               "LastName": "Wang",  
               "Balance": "-50",  
               "Email": "connorwang2@gmail.com",  
               "Fav_Restraunts":["Chipolte", "Panda Express", "Board and Brew"],
               "Least_Fav_Restraunts":["IHop", "Luna Grill"]
              })  

#print(InfoDb[0]["Fav_Restraunts"][1])
#print(InfoDb[1]["Fav_Restraunts"][0])

def print_data(n):
    print(InfoDb[n]["LastName"], InfoDb[n]["Balance"], InfoDb[n]["Email"])  # using comma puts space between values
    print("\t", "Favorite Restraunts: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Fav_Restraunts"]))  # join allows printing a string list with separator
    print()

#self explanatory procedure. Getting certain datat with few guidelines on format like commas and spaces to neaten up. n creates itteration.
  
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
#for loop i shown as seen with "for"
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return
#While loop is shown as seen with "while"

def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return 
#recursive since we keep checking condition, and in the mean time continue to print. And once that codition is met, and we have printed each part of the list, we can return and leave the process


def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion

