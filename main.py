import random


print("Welcome to Rock, Paper and Scissors")

options = ["R", "P", "S"]

def game(user, cpu):
    if user == "R" and cpu == "S":
        print("USER WINS!")
    elif user == "P" and cpu == "R":
        print("USER WINS!")
    elif user == "S" and cpu == "P":
        print("USER WINS!")
    elif user == cpu:
        print("TIE!")
        start()
    else:
        print("CPU WINS!")


print("Game Options: R for Rock || P for Paper || S for Scissors")


def start():
    while True:
        cpu = random.choice(options)
        user = input("Select an option: ")
        if user == "R" or user == "P" or user == "S":
            print(f"USER ({user}): CPU ({cpu})")
            game(user, cpu)
            break

start()


