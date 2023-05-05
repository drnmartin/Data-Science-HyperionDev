# DROPBOX T04 COMPULSORY TASK 1
# Note: In this longer task, it really helped to plan the task using my comments numbering. 
# This made it easier for me to identify the bits that I found easy and got those out of the way early e.g. the early input statements.
# I then could focus on getting the if control structure correct and understanding the awards system.
# I have written the code to take integer values of minutes for simplicty as more detailed time values were not explicitly requested in the task.

# (1) Ask user for the swimming, cycling and running event time

swimming_time = input("\n\nPlease enter your swimming time in the triathlon in minutes:\n")
cycling_time = input("\n\nPlease enter your cycling time in the triathlon in minutes:\n")
running_time = input("\n\nPlease enter your running time in the triathlon in minutes:\n")

# (2) Calculate and display the total time taken to complete the triathlon

total_time = int(swimming_time) + int(cycling_time) + int(running_time)
print("\n\nYour total time taken to complete the triathlon was " + str(total_time) + " minutes.\n")


# (3) Inform participant that the qualifying time for awards is 100 minutes

print("\nThe qualifying time for awards is 100 minutes.\n")


# (4) Inform the participant whether they have received an award or not and, if so, which one.

QUALIFYING_TIME = 100

if  total_time <= QUALIFYING_TIME:

    print("\nYour result is within the qualifying time and so you will receive the Provincial Colours Award.\n")

elif  total_time > QUALIFYING_TIME and total_time <= (QUALIFYING_TIME +5):

    print("\nYour result is within 5 minutes of the qualifying time and so you will receive the Half Provincial Colours Award.\n")

elif  total_time > (QUALIFYING_TIME +5) and total_time <= (QUALIFYING_TIME +10):

    print("\nYour result is within 10 minutes of the qualifying time and so you will receive the Provincial Scroll.\n")

else:

    print("\nUnfortunately, your time was more than 10 minutes more than the qualifying time and so you will not receive an award. Please enter again next year!\n")