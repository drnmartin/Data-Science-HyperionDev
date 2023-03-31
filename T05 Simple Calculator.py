# T05 Compulsory Task 1 Capstone Project 1 - Variables and Control Structures

# Note (1): I wanted to display 2dp in the values as you would expect with currencies.
# I looked this up on https://pythonhow.com/how/limit-floats-to-two-decimal-points/

# Note (2) I wanted this initial screen to be friendlier that the one in the task instruction.
# So I added a welcome note and numbered the two options.
 
# Note (3) I wanted to ensure that 2 digits were always shown after the decimal point.
# I looked this feature up on: https://stackoverflow.com/questions/45310254/fixed-digits-after-decimal-with-f-strings

# (1) Import the math built-in module which extends use of mathematical functions.

import math

# (2) Let the user know that there are two calculator types to choose from.

print("\nWelcome. You have a choice of two calculator types.")
print("\nCalculator 1: investment - to calculate the amount of interest you'll earn on your investment")
print("Calculator 2: bond - to calculate the amount you'll have to pay on a home loan\n")

selection = input("Enter either 'investment' or 'bond' from the menu above to proceed:\n")

# (3) Whatever case they enter their answer of investment or bond, it should register as a valid entry.

selection_lower = selection.lower()

# (4a) Running the bond calculator: Collect data from user

if selection_lower == "bond":

    house_value = float(input("Please enter the present value of the house (£):"))
    bond_interest_rate = float(input("Please enter the interest rate (%):"))
    months = float(input("Please enter the number of months required to repay the bond:"))

# (4b) Running the bond calculator: Monthly repayment calculator

    monthly_bond_interest = bond_interest_rate / 1200
    repayment_topline = house_value * monthly_bond_interest
    repayment_bottomline = 1 - (1 + monthly_bond_interest) ** -months
    repayment = repayment_topline / repayment_bottomline
    repayment_2dp = round(repayment, 2)

    print("________________________________________________________________")
    print(f"House value (£): {house_value:.2f}")
    print(f"Bond interest rate (%): {bond_interest_rate:.2f}")
    print(f"Loan repayment duration (months): {months:.2f}")
    print(f"Monthly repayment amount (£): {repayment_2dp:.2f}")
    print("________________________________________________________________")


# (5a) Running the investment calculator: Collect data from user (including correct spelling of simple or compound or give error)

elif selection_lower == "investment":

    deposit = float(input("Please enter the amount of money you are deposting (£):"))
    interest_rate = float(input("Please enter the interest rate (%):"))
    years = float(input("Please enter the number of years that you plan on investing:"))
    interest = input("Please enter whether you would like simple or compound interest:")
    interest_lower = interest.lower()

# (5b) Running the investment calculator: Simple interest calculator

    if interest_lower == "simple":
        
        simple_interest = deposit * (1 + (interest_rate * years / 100))
        simple_interest_2dp = round(simple_interest, 2)

        print("________________________________________________________________")
        print(f"Deposit amount (£): {deposit:.2f}")
        print(f"Interest rate (%): {interest_rate:.2f}")
        print(f"Investment duration (years): {years:.2f}")
        print("Interest type = Simple")
        print(f"Principal amount and interest (£): {simple_interest_2dp:.2f}")
        print("________________________________________________________________")

# (5c) Running the investment calculator: Compound interest calculator

    elif interest_lower == "compound":

        compound_interest = (deposit) * math.pow((1 + (interest_rate / 100)), years)
        compound_interest_2dp = round(compound_interest,2)

        print("________________________________________________________________")
        print(f"Deposit amount (£): {deposit:.2f}")
        print(f"Interest rate (%): {interest_rate:.2f}")
        print(f"Investment duration (years): {years:.2f}")
        print("Interest type = Compound")
        print(f"Principal amount and interest (£): {compound_interest_2dp:.2f}")
        print("________________________________________________________________")

    else:
        print("Invalid entry. Please start again.")

# (6) Neither bond or investment was selected.

else:
   print("You have not entered a correct option. Please try again.")
