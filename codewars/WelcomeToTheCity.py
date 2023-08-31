def say_hello(name, city, state):
    firstname = input("Please enter your first name")
    lastname = input("Please enter your last name")
    name = [firstname,lastname]
    city = input("What City are you from?")
    State = input("Which state are you from")
    print("Hello" + name + "! Welcome to" + city + "," + state)