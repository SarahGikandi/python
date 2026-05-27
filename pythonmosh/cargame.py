command = ""
started = False
while command != True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("You are already started")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is alredy stopped")
        else:
            started = False
            print("Car stopped.")
    elif command =="help":
        print("""
start - to start the car
stop - car stopped
quit - to quit""")
    elif command == "quit":
        break
    else:
        print("Sorry, I dont understand that")
