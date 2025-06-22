from itertools import count

def isoelectric_point():
    try:
        count = int(input("Enter the number of pKas: "))
        if count not in [2, 3]:
            print("Error: Please enter a pKas between 2 and 3!")
            return

        pKa = []
        for i in range(count):
            value = float(input("Enter the pKa " + str(i+1) + ": "))
            pKa.append(value)

        if count == 2:
            pI = sum(pKa) / 2
        else:
            print("If you gave 3 pKas, please give me, which two is used for pI counting:")
            idx1 = int(input("Enter the first index from 1: ")) - 1
            idx2 = int(input("Enter the second index: ")) - 1

            if any(i not in range(3) for i in [idx1, idx2]):
                print("Error: Please enter a pKas between 1 and 3!")
                return

            pI = (pKa[idx1] + pKa[idx2]) / 2

        print(f"The isoelectric point is: {pI}")

    except ValueError:
        print("Error: Please enter a number!")

isoelectric_point()
