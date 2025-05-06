

import math

def pondus_hidrogenii():
    try:
        acid_or_base = input("Please enter an acid or base: ").strip().lower()

        if acid_or_base not in ['acid', 'base']:
            print("Error: please enter an acid or_base: ")
            return

        conc = float(input("Please enter concentration (mol/L): "))
        if conc <= 0:
            print("Error: the given value is not positive. Please try again.")
            return

        if acid_or_base == 'acid':
            pH = -math.log10(conc)
        else:
            pOH = -math.log10(conc)
            pH = 14 - pOH

        print(f"The pH value is: {pH}")

        if pH < 7:
            print("The solution is acidic")
        elif pH == 7:
            print("The solution is neutral")
        else:
            print("The solution is alkaline")

    except ValueError:
        print("Error: please enter an acid or_base: ")


print(pondus_hidrogenii())

