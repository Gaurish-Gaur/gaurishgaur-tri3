InfoDb = []
# List with dictionary records placed in a list  
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

#print(InfoDb[0]["Fav_Restraunts"][1])
#print(InfoDb[1]["Fav_Restraunts"][0])

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



def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion
if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   tester()
