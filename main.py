"""
version 1.0: Base
v1.1.0: Setting the foundations with the 3 main options
v1.1.1: Added the option to invest money
v1.1.2: Add a relationship between invested money and investment location

version 1.2
v1.2.0: Added the database in a txt file
"""

import os

# Function to load data from a file
def cargar_datos(archive_name):
    if os.path.exists(archive_name):
        with open(archive_name, 'r') as archive:
            lines = archive.readlines()
            if lines:
                user = lines[0].strip()
                balance = float(lines[1].strip())
                investments = [line.strip() for line in lines[2:]]
                return user, balance, investments
    return "", 0.0, []

# Function to save data to a file
def save_data(archive_name, user, balance, investments):
    with open(archive_name, 'w') as archive:
        archive.write(f"{user}\n")
        archive.write(f"{balance}\n")
        for inv in investments:
            archive.write(f"{inv}\n")
    print(f"Data saved in {archive_name}")

# Function to read and display the content of the file
def show_archive(archive_name):
    if os.path.exists(archive_name):
        with open(archive_name, 'r') as archive:
            content = archive.read()
            print("\nFile content:")
            print(content)
    else:
        print(f"The file {archive_name} does not exist.")

# Load data at the beginning
archive_name = 'datos.txt'
user, balance, investments = cargar_datos(archive_name)

if not user:
    user = input("User: ")
    start = float(input("initial account money: "))
    balance = start  # To keep track of the account balance
state = True

while state:
    print("\nEnter the number of what you want to do")
    print("Enter ? to watch things you can do\n")
    thing = input(f"what do you want to do {user}: ").lower()
    match thing:
        case "?":
            print("1 = Deposit")
            print("2 = Retire")
            print("3 = Invest (It will be quit from the balance)")
            print("a = Watch amount and balance")
            print("x = quit")
        case "1":
            amount = float(input("Deposit an amount:"))
            balance += amount
        case "2":
            amount = float(input("Retire an amount:"))
            balance -= amount
            if balance <= 0:
                print("\nYOU ARE BROKE\nGET MONEY")
        case "3":
            investmoney = float(input("Insert money you invested:"))
            investplace = input("Where you have invested: ")
            balance -= investmoney
            investments.append(f"{investmoney} : {investplace}")
        case "a":
            print(f"Balance:\t{balance}\n")
            for i in investments:
                print(f"[Investment] {i}")
        case "x":
            print(f"your balance is: {balance}$")
            state = False

    # Save data after each operation
    save_data(archive_name, user, balance, investments)

    # Display file content after saving
    show_archive(archive_name)
