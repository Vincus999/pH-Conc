import math

# Adding the value of the concentration "c" of the strong base
c = float(input("Please give me the value of the concentration in mol/l (c): "))

# Checking the positivity of the given value
if c <= 0:
    print("Error: the given value is not positive. Please try again.")
else:
    # Counting the pOH
    pOH = -math.log10(c)

    # Counting the pH of the strong base
    pH = 14 - pOH


    # Printing the pH value
    print(f"The pH of the strong acid: {pH} ")



