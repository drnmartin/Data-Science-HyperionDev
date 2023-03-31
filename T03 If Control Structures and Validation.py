# COMPULSORY TASK 1
# Note: Used \n to space out the responses. 

# (1) Ask the user to input their full name

full_name = input("What is your full name?\n\n")

# (2) Then split the string into separate words. Then assign a variable to the number of words.

full_name_split = full_name.split()
full_name_split_len = len(full_name_split)

# (3) Perform validation check (1) No entry is given.

if len(full_name) == 0:
    print("\nYou haven't entered anything. Please enter your full name.\n")


# (4) Perform validation check (2) At least two names have been entered.

elif full_name_split_len <= 1:
    print("\nYou must enter both your first name and your surname.\n")


# (5) Perform validation check (3) String length is less than 4 characters.

elif len(full_name) < 4:
    print("\nYou have entered less than 4 characters. Please make sure that you have entered your name and surname.\n")


# (6) Perform validation check (4) String length is greater than 25 characters.

elif len(full_name) > 25:
        print("\n\nYou have entered more than 25 characters. Please make sure that you have only entered your full name.\n")


# (7) Closing else clause if all checks have been passed.

else:
    print("\n\nThank you for entering your name.\n")