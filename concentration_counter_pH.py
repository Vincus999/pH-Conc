import math

# Adding the pH value of the strong acid
pH = float(input("Please give me the value of the pH: "))

# Checking the positivity of the given value
if pH < 0:
    print("Error: the given value is not positive. Please try again.")
else:
    # Counting the concentration of the strong acid from pH
    c = 10 ** (-pH)


    # Printing the concentration
    print(f"The concentration of the strong acid: {c} mol/l")



