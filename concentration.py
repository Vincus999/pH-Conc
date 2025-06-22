
def concentration():
   try:
       pH = float(input("Please give me the value of the pH: "))
       if pH < 0 or pH > 14:
           print("Please give me the value between 0 and 14")
           return

       if pH <= 7:
           h_conc = 10 ** (-pH)
           print(f"The concentration is:  {h_conc} mol/L")

       else:
           pOH = 14 - pH
           oh_conc = 10 ** (-pOH)
           print(f"The concentration is:  {oh_conc} mol/L")

   except ValueError:
       print("Please give me the value between 0 and 14")


concentration()


