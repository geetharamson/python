#Given an integer N (between 1 and 5) and a string S: "one", "two", "three", "four" or "five” (only) returns the result of multiplying N and S expressed as an integer. For example, given N = 4 and S = "two", your function should return 8.

def multiply(number, stringNumber):
  # validate the first parameter
  if (number < 1 or number > 5):
    print(f"Invalid first input: {number}. It must be between 1 and 5")
    return

  # validate the second parameter
  stringToNumberDictionary = {"one": 1, "two": 2, "three": 3, "four":4, "five":5}
  if stringNumber not in stringToNumberDictionary:
    print(f"Invalid second input: {stringNumber}. It must be one of {stringToNumberDictionary.keys()}")
    return

  # covert stringNumber into a number
  secondNumber = stringToNumberDictionary.get(stringNumber)

  # do the multiplication
  result = number * secondNumber
  print(f"{number} x {stringNumber} = {result}")


print("\n*** Test invalid first parameter ***")
print("====================================")
multiply(10, "two")
multiply(-1, "five")
multiply(0, "one")

print("\n*** Test invalid second parameter ***")
print("=====================================")
multiply(2, "Two")
multiply(3, "THREE")
multiply(4, "two hundred")

print("\n*** Test invalid first and second parameter ***")
print("\n===============================================")
multiply(22, "twenty")
multiply(-4, "FoUR")

print("\n*** Test invalid Null ***")
print("\n=========================")
multiply(4, "")


print("\n*** Test valid values ***")
print("==========================")
multiply(3, "three")
multiply(5, "two")
