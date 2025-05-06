
import math

def henderson_hasselbach():
    try:
        pKa = float(input("Please give me the pKa value : "))
        A_conc = float(input("Please give me the acid concentration value (mol/L) : "))
        HA_conc = float(input("Please give me the weak acid concentration value (mol/L) : "))

        if A_conc <= 0 or HA_conc <= 0:
            print("Error: the given value is not positive. Please try again.")
            return

        pH = pKa + math.log10(A_conc / HA_conc)
        print(f"The pH value is: {pH}")

    except ValueError:
        print("Error: the given value is not valid. Please try again.")


print(henderson_hasselbach())
