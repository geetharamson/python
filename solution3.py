#Count no of Ones. Given N = 13 the function should return 6, because: all the positive integers that do not exceed 13 are 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 and 13
#Digit 1 occurs six times altogether: once in number 1, once in number 10, twice in number 11, once in number 12, and once in number 13. For this problem, N is an integer within the range [0...100]

def countOnes(number):
	if (type(number) != int):
		print("invalid input")
		return
        
	if (number < 0 or number > 100):
		print("input out of range")
		return
        
	numberOfOnes = 0
    
	for x in range(number + 1):
		stringX = str(x)
		numberOfOnes += stringX.count("1")
        
	return numberOfOnes
        

# Tests

print(f"number of ones for 0 = {countOnes(0)}")
print(f"number of ones for 13 = {countOnes(13)}")
print(f"number of ones for 10 = {countOnes(10)}")

# Test out of range
print(f"number of ones for 200 = {countOnes(200)}")
print(f"number of ones for -13 = {countOnes(-13)}")
print(f"number of ones for 10.2 = {countOnes(10.2)}")