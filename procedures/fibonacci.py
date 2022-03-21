def fibo(n):
	if n <= 0:
		return [0]
	s = [0,1]
	while len(s) < n:
		hold = len(s)
		rec = s[hold - 1] + s[hold - 2]
		s.append(rec)
	return s
#
def tester():
    n = int(input("Enter #: "))
    # check if the number is negative since those won't work
    if n < 0:
        print("No negative numbers")
    else:
        print("The fibonacci Terms of", n, "is", fibo(n), "!")
#formats answers given in a clear to read wway with input and output

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   tester()
