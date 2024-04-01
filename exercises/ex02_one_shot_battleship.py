"""EX01 - One Shot Battleship."""

__author__ = "730649327"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2


guess_row: int = int(input("Guess a row: "))
while guess_row > grid_size or guess_row < 1:
    guess_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
guess_column: int = int(input("Guess a column: "))
while guess_column > grid_size or guess_column < 1:
    guess_column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))   

result_box: str = ""
if guess_row == secret_row and guess_column == secret_column:
    result_box = RED_BOX
else:
    result_box = WHITE_BOX

current_row: int = 1
while current_row <= grid_size:
    emoji_output: str = ""
    current_column: int = 1
    if guess_row == current_row:
        while current_column <= grid_size:
            if guess_column == current_column:
                emoji_output += result_box
            else: 
                emoji_output += BLUE_BOX
            current_column += 1
    else:    
        while current_column <= grid_size:
            emoji_output += BLUE_BOX
            current_column += 1
    print(emoji_output)
    current_row += 1


if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")      
elif guess_row == secret_row and guess_column != secret_column:
    print("Close! Correct row, wrong column.")
elif guess_column == secret_column and guess_row != secret_row:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")