 #Days of the week are represented as three-letter strings ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun") Given a string S representing the day of the week 
#and an integer N (between 0 and 50, inclusive), returns the day of the week that is K days later. For example, if S = "Wed" and N = 2, the function should return "Fri".
#Given S = "Sat" and N = 23, the function should return "Mon". 

  def findDay(currentDay, number):
	validDays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
	if (currentDay not in validDays):
		print("Invalid current Day input")
		return

	if (type(number) != int):
		print("invalid number type. It should be an integer between 0 and 50")
		return
        
	if (number < 0 or number > 50):
		print("invalid number input. It should be between 0 and 50")
		return
        
	currentDayPosition = validDays.index(currentDay)
	positionAfterAddingInput = currentDayPosition + number
	indexOfResultDay = positionAfterAddingInput % 7
    
	return validDays[indexOfResultDay]
        

# Valid Tests

day = findDay("Wed", 2)
print(f"Wed + 2 = {day}")

day = findDay("Sat", 3)
print(f"Sat + 3 = {day}")

day = findDay("Mon", 7)
print(f"Mon + 7 = {day}")

day = findDay("Sat", 23)
print(f"Sat + 23 = {day}")        
        
       

# Out of range tests

day = findDay("Sun", 67)
print(f"Sun + 67 = {day}")

day = findDay("", 23)
print(f"+ 23 = {day}")

day = findDay("wed", 23)
print(f"wed + 23 = {day}")

day = findDay("saT", 2)
print(f"saT + 23 = {day}")


day = findDay("Sat", 2.3)
print(f"Sat + 2.3 = {day}")

day = findDay("Sat", -9)
print(f"Sat + -9= {day}")

day = findDay("Fri", 50)
print(f"Fri + 50 = {day}")

day = findDay("Fri", 51)
print(f"Fri + 51 = {day}")