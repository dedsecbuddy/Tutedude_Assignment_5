result = {
    "mike" : 98.5,
    "john" : 70,
    "alice" : 85,
    "max" : 89
}

print("Welcome!")

while True:
    name = input("Please enter your name to check the marks:").lower()
    if name in result:
        print(f"Hey {name.title()}, You scored : {result[name]}, Congratulations!")
        break
    else:
        print("No name found,Try Again!")
