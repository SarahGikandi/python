temperature = 30

if temperature > 30:
    print("Its a hot day")
else:
    print("Its a cold day")

if temperature == 30:
    print("same")
else:
    print("Not same")

if temperature != 30:
    print("not equal to 30")
else:
    print("equal to 30")

name = input("Enter your name: ")
x = (len(name))
if x < 3:
    print("Name must be at least 3 characters")
elif x > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good")
