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