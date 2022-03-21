{% include replits.html %}

# Week 1

# Lists and Loops

## Code snippets

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
