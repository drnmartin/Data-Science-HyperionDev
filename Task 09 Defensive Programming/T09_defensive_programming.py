# T09 COMPULSORY TASK: SIMPLE CALCULATOR APPLICATION

# (A) Extending the program with options to either enter data or read data from file.

# (A1) Needed a quick exit at the bottom of the code. So found the sys exit option below.
# https://www.interviewkickstart.com/learn/python-exit-commands

import sys

# (A2) Welcome and user options for data entry or data collection.

while True:
    border = ("_" * 80)
    print(border)
    print("\nHello. You can enter data here to write to a file or read data from a file.")
    print(border)
    option = input("\nPlease enter '1' for reading data from a file or '2' for entering data: ")

    # (A3) Taking user input of filename to read data from.
    # THE TASK STATES THAT ONLY THE EQUATION SHOULD BE READ FROM THE FILE AND THE RESULT CALCULATED BY THE PROGRAM AND PRINTED TO SCREEN.

    if option in "12":
        if option == "1":
            filename = input("\nPlease enter the name of your .txt file: ")
            file = None
            try:
                file = open(f'{filename}.txt', 'r')
                data = file.readlines()
                print(border)
                print(f"The data is your file {filename}.txt is as follows:\n")

                for line in data:
                    num1, operator, num2 = line.split()
                    num1 = float(num1)
                    num2 = float(num2)

                    # (A4) Run the calcuations within an if statement.

                    if operator == "*":
                        result = num1 * num2      
                    elif operator == "+":
                        result = num1 + num2
                    elif operator == "-":
                        result = num1 - num2
                    elif operator == "/":
                        result = num1 / num2
                
                    # (4) Print the equations plus the resuls to the screen.
                    
                    equation = (f"{num1:.2f} {operator} {num2:.2f} = {result:.2f}")  
                    print(equation)
                print(border)
                break

            # (A5) Handling the file not found problem.
            
            except FileNotFoundError:
                print("\nThe file that you are trying to open does not exist. Please try again.")
            finally:
                if file is not None:
                    file.close()
        
        # (B) This option is for when the user wishes to enter the equation.
        # (B1) Welcome to the calculator message.
        
        else:    
            border = ("_" * 80)
            print(border)
            print("\nWelcome. This is a simple calculator that takes in two numbers and an operator.")
            print(border)

            # (B2) Ask user to enter two numbers and the operation, checking for exceptions.

            while True:

                while True:
                    try:    
                        num1 = float(input("\nPlease enter your first number: "))
                        break
                    except ValueError:
                        print("\nThat is not a valid number. Please try again.") 

                while True:
                    operator = (input("\nPlease enter one of the following operators ( + - * / ) : "))
                    if operator in "+-*/":
                        break
                    else:
                        print("\nThat is not a valid entry. Please try again.")       

                while True:
                    try:    
                        num2 = float(input("\nPlease enter your second number: "))
                        break
                    except ValueError:
                        print("\nThat is not a valid number. Please try again.") 

                # (B3) Run the calcuations within an if statement.

                if operator == "*":
                    result = num1 * num2      
                elif operator == "+":
                    result = num1 + num2
                elif operator == "-":
                    result = num1 - num2
                elif operator == "/":
                    result = num1 / num2
                
                # (B4) Print the result and append only the equation to the file. 
                # THE TASK STATES THAT ONLY THE EQUATION SHOULD BE SENT TO THE FILE AND THE RESULT ONLY PRINTED TO SCREEN.
                
                equation = (f"{num1:.2f} {operator} {num2:.2f} = {result:.2f}")  
                equation2 = (f"{num1:.2f} {operator} {num2:.2f}") 
                print()
                print(equation)
                print()
                with open("user_equations.txt", "a") as file:
                    file.writelines(equation2 + "\n")

                # (B5) Instructions to see if user wishes to add any more equations.

                while True:    
                    continue_program = input("Would you like to enter another equation? (Y/N): ")
                    if continue_program.lower() in "yn":
                        break
                    else:
                        print("\nThat is not a valid entry. Please try again.\n")
                
                if continue_program.lower() == "n":
                    print(border)
                    print("\nYou have exited the program.")
                    print(border)
                    sys.exit(0)

    else:
        print("\nThat is not a valid entry. Please try again.\n")
        