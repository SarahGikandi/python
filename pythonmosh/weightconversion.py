#weight = int(input("Weight: "))
weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    converted= int(weight) * 0.45
    print(f"you are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"you are {converted} pounds")