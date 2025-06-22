


def lambert_beer():
    try:
        eps = float(input("Please give me the epsilon value (L/molcm: "))
        A = float(input("Please give me the absorbance value: "))
        l = float(input("Please give me the cuvette size (cm): "))

        if eps < 0 or l <= 0:
            print("Error: The given value is not positive. Please try again.")
            return

        conc = A / (eps * l)
        print(f"The concentration is: {conc}")

    except ValueError:
        print("Error: The given value is not valid. Please try again.")

lambert_beer()