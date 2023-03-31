# T11 COMPULSORY TASK STRING MANIPULATIONS
# It took some trial and error to put the space in the right place for the second alogrithm.

# (1) User inputs a string.

string = input("\nPlease enter your phrase that requires manipulation: ")
border = "-" * 90
print(border)
print(f"\nYour original string: {string}")

# (2) Running a for loop to alternate the cases for each letter.

result = ""

for each in range(len(string)):
    if each % 2 == 0:
        result += string[each].upper()
    else: 
        result += string[each].lower()

print(f"\nAlgorithm applied - Alternating cases for letters: {result}")

# (3) Running a for loop to alternate the cases for each word. First split the string into a list.

string_split = string.split()
result2 = ""

for each in range(len(string_split)):
     if each % 2 != 0:
         result2 += " " + string_split[each].upper()
     else: 
         result2 += " " + string_split[each].lower()

print(f"\nAlgorithm applied - Alternating cases for words: {result2}")
print(border)
