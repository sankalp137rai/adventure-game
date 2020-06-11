import time
import random


def print_pause(message):
	print(message)
	time.sleep(2)


def intro():
	print_pause("You find yourself standing in an open field,"
	             " filled with grass and yellow wildflowers.")
	print_pause("Rumor has it that a wicked fairie is somewhere"
	             " around here, and has been terrifying the nearby village.")
	print_pause("In front of you is a house.")
	print_pause("To your right is a dark cave.")
	print_pause("In your hand you hold your trusty (but not very effective) dagger.\n")


def play_again():
    response=input("Would you like to play again?(y/n)")
    if response=="y":
   		print_pause("Excellent! Restarting the game ...")
   		game()
    elif response=="n":
   		print_pause("Thankyou for playing! see you next time.")
    else:
   	    play_again()	


def field(items,enemy):
	print_pause("Enter 1 to knock on the door of the house.")
	print_pause("Enter 2 to peer into the cave.")
	print_pause("what would you like to do?\n(Please enter 1 or 2.)")
	response(items,enemy)


def run_away(items,enemy):
	print_pause("You run back into the field. Luckily, you don't"
		         " seem to be followed.\n")
	field(items,enemy)


def fight(items,enemy):
	if "Ogoroth" in items:
		print_pause(f"As the {enemy} moves to attack, you unsheath your new sword.")
		print_pause("The sword of Ogoroth shine brightly in you hand as you brace"
			           " your self for attack.")
		print_pause(f"But {enemy} take one look at your shiny toy and ran away!")
		print_pause(f"You have rid the town of {enemy}. You are victorius!")
		play_again()
	else:
		print_pause("You do your best...")
		print_pause(f"But your dagger is no match for {enemy}")
		print_pause("You has been defeted!")
		play_again()


def cave(items,enemy):
	if "Ogoroth" in items:
		print_pause("You peer cautiously into the cave.")
		print_pause("You've been here before, and gotten all the good stuff"
			           "it's just an empty cave now.")
		print_pause("You walk back out to the field.\n")
		field(items,enemy)
	else:
		print_pause("You peer cautiously into the cave.")
		print_pause("It turns out to be only very small cave.")
		print_pause("Your eyes catches glint of metal behind the rock.")
		print_pause("You have found magical Sword of Ogoroth!")
		print_pause("You discard your silly old dagger and take sword with you.")
		print_pause("You walk back out to the field.\n")
		items.append("Ogoroth")
		field(items,enemy)


def house(items,enemy):
	print_pause("You approach the door of the house.")
	print_pause(f"You are about to knock  when the door opens and out step a {enemy}")
	print_pause(f"Eep! this is the {enemy}'s house!")
	print_pause(f"The {enemy}'s attack on you")
    response=input("Would you like to (1) fight or (2) run away?")
    if response=="1":
        fight(items,enemy)
    elif response=="2":
		run_away(items,enemy)
	else:
		play_again()


def response(items,enemy):
	choice=input()
	if choice=="1":
		house(items,enemy)
	elif choice=="2":
		cave(items,enemy)
	else:
		print("(Please enter 1 or 2.)")
   		response(items,enemy)


def game():
    items=["dagger"]
    enemys=["pirate", "troll", "gorgon", "wicked fairie", "dragon"]
    enemy=random.choice(enemys)
    intro()
    field(items,enemy)


game()