import time
import random


def print_pause(string):
    print(string)
    time.sleep(1)


def intro(creatures):
    print_pause("You find yourself standing in a corn field, "
                "a perfect blue sky above you.")
    print_pause(f"There is a rumour that a {creatures} "
                "has been lurking around here for hundreds of years.\n")
    print_pause("To your left is a small old house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold a small knife: "
                "a valued object, but not a very effective weapon.\n")


def cave(items, creatures, weapons):
    if weapons in items:
        print_pause("You walk into the dark cave.")
        print_pause(f"You already picked up the {weapons} you found earlier.")
        print_pause("There is nothing more to do here.")
        print_pause("You walk back into the field.\n")
        field(items, creatures, weapons)
    else:
        print_pause("There is no one in the cave, it is dark and quiet.")
        print_pause("With the corner of your eye "
                    "you catch a glimpse of a shiny object.")
        print_pause(f"It is a {weapons}!")
        print_pause("You pick it up, might prove useful!\n")
        items.append(weapons)
        print_pause("You walk back into the field.\n")
        field(items, creatures, weapons)


def field(items, creatures, weapons):
    print_pause("Enter 1 to open the door of the house.")
    print_pause("Enter 2 to walk into the cave.")
    choice = input("What would you like to do?\n"
                   "(Please enter 1 or 2).\n")
    if choice == '1':
        house(items, creatures, weapons)
    elif choice == '2':
        cave(items, creatures, weapons)
    else:
        print_pause("Try again!")
        field(items, creatures, weapons)


def house(items, creatures, weapons):
    print_pause(f"A {creatures} jumps out of the house!")
    choice2 = input("Do you choose to fight (1) or run (2)?\n"
                    "(Please enter 1 or 2).\n")
    if choice2 == '2':
        print_pause("You run back into the empty field.\n")
        field(items, creatures, weapons)
    elif choice2 == '1':
        fight(items, creatures, weapons)
    else:
        print_pause("Try again!")
        house(items, creatures, weapons)


def fight(items, creatures, weapons):
    if weapons in items:
        print_pause(f"You pick up your found {weapons} and BOOM!")
        print_pause(f"The {creatures} shrieks in pain.")
        print_pause(f"You defeated the {creatures}!")
        print_pause("Congratulations, you mighty warrior!\n")
        play_again()
    else:
        print_pause(f"You fiercely throw your knife towards the {creatures}.")
        print_pause(f"The {creatures} is strong, you need a better weapon!")
        print_pause(f"The {creatures} kills you!")
        print_pause("You lose!\n")
        play_again()


def play_again():
    while True:
        again = input("Do you want to play again (yes/no)?\n").lower()
        if "yes" in again:
            print_pause("Wonderful! Restarting...\n")
            play_game()
            break
        elif "no" in again:
            print_pause("Thank you for playing!")
            break
        else:
            print_pause("I am sorry, I don't understand.")


def play_game():
    items = []
    weapons = random.choice(["diamond sword", "machete", "steel axe"])
    creatures = random.choice(["werewolf", "goblin", "demogorgon", "basilisk"])
    intro(creatures)
    field(items, creatures, weapons)


play_game()
