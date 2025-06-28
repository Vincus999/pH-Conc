


def saturation():
    try:
        P_conc = float(input("Please give me the protein concentration (mol/L): "))
        PL_conc = float(input("Please give me the complex concentration (mol/L): "))

        if P_conc < 0 or PL_conc < 0:
            print("Error: Please enter positive values")
            return

        theta = (PL_conc / (PL_conc * P_conc)) / 100
        print(f"The rate of saturation: {theta}")

    except ValueError:
        print("Error: Please enter positive values")

saturation()

