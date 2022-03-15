def fibo(n):
	if n < 0:
		print("No negative numbers")

	if n == 0:
		return 0
	if n==1 or n==2:
		return 1

	else:
		return fibo(n-1) + fibo(n-2)


def tester():
    num = int(input("Enter #: "))
    # check if the number is negative
    if num < 0:
        print("No negative numbers")
    else:
        print("The fibonacci of", num, "is", fibo(num))

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   tester()
