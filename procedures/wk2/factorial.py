class F:
  def __call__(self, num):
    final = 1 #for zero or one
    for i in range(1, num + 1): #range is non exclusive, needs to stop at num, not at right before num
      final *= i
    return final

factorial = F()
number = input("Factorial for: ")
number = int(number)
print("The factorial of ", number, "is",   factorial(number))