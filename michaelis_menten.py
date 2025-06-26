

def michaelis_menten():
    try:
        S_conc = float(input('Enter concentration of the substrate (mol/mL): '))
        V_max = float(input('Enter maximum velocity of the reaction (mol/s): '))
        KM = float(input('Enter the Michaelis-constant (mol/ml): '))

        if S_conc < 0 or V_max < 0:
            print('Error: Please enter positive values')
            return


        V0 = (V_max * S_conc) / (KM + S_conc)
        print(f"The reaction velocity is {V0} mol/s!")

    except ValueError:
        print('Error: Please enter a number')

michaelis_menten()

