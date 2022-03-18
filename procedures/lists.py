InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Gaurish",  
               "LastName": "Gaur",  
               "Paid": "0",  
               "Email": "gaurishgaur3@gmail.com",   
               "Event":["Parli","PF","LD"]  
              })  

InfoDb.append({  
               "FirstName": "Sara",  
               "LastName": "Beniwal",  
               "Paid": "50",  
               "Email": "sarabeniwalsd@gmail.com ",  
               "Event":["PF","Speech"]  
              })  
InfoDb.append({  
               "FirstName": "Aniruffffff",  
               "LastName": "Ramachandran",  
               "Paid": "-1000",  
               "Email": "Anigumpthemonkey@gmail.com",  
               "Event":["Cheer"]  
              })  

print(InfoDb[0]["Event"][1])