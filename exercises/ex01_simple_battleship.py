"""EX01 - Simple Battleship - A cute step toward Battleship."""

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

__author__ = "730649327"


p1_location = input("Pick a secret boat location between 1 and 4: ")
if int(p1_location) < 1:
    print(f"Error! {p1_location} too low!")
    exit()

if int(p1_location) > 4:
    print(f"Error! {p1_location} too high!")
    exit()

p2_guess = input("Guess a number between 1 and 4: ")
if int(p2_guess) < 1:
    print(f"Error {p1_location} too low!")
    exit()

if int(p2_guess) > 4:
    print(f"Error {p1_location} too high!")
    exit()


emoji_output = ""


if p2_guess == p1_location and p1_location == "1":
    emoji_output = RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX 
elif p2_guess == "1":
    emoji_output = WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX 

if p2_guess == p1_location and p1_location == "2":
    emoji_output = BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX 
elif p2_guess == "2":
    emoji_output = BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX 

if p2_guess == p1_location and p1_location == "3":
    emoji_output = BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX 
elif p2_guess == "3":
    emoji_output = BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX  

if p2_guess == p1_location and p1_location == "4":
    emoji_output = BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX 
elif p2_guess == "4":
    emoji_output = BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX 

print(emoji_output)
if p2_guess == p1_location:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")