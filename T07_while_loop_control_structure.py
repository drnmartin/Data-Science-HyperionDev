# T07 Compulsory Task: While Loops
# I have reused the 2dp rule for the results

# (1) Ask the user to enter a number.

total = 0
count = 0

# (2) When the user enters -1, the program stops requesting the user to enter a number.

while True:
    num = float(input("\nPlease enter a number (Enter -1 to exit):"))

    if num == -1:
        break

    total += num
    count += 1

average = total / count

# (3) The program then calculates the average of the numbers entered, excluding the -1.

print ("_______________________________________________________")
print(f"\nThe sum of the numbers you entered is (2 dp): {total:.2f}")
print(f"\nThe count of the numbers you entered is: {count}")
print(f"\nThe average of the numbers you entered is (2 dp): {average:.2f}")
print ("_______________________________________________________")       
