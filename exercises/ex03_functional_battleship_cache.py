"""EX03 - Functional Battleship."""

__author__ = "730649327"
import random

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(grid_size: int, row_or_column: str) -> int:
    """Prompt and return guess row or column."""
    assert row_or_column == "row" or row_or_column == "column"
    guess = int(input(f"Guess a {row_or_column}:"))
    while guess > grid_size or guess < 1:
        guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again:"))
    return (guess)
   

def print_grid(grid_size: int, guess_row: int, guess_column: int, guess_correctness: bool) -> None:
    """Print emoji output and grid."""
    result: str = ""
    if guess_correctness:
        result += RED_BOX
    else:
        result += WHITE_BOX
    row_counter: int = 1
    while row_counter <= grid_size:
        column_counter: int = 1
        emoji_output: str = ""
        if row_counter == guess_row:
            while column_counter <= grid_size:
                if column_counter == guess_column:
                    emoji_output += result
                else:
                    emoji_output += BLUE_BOX
                column_counter += 1
        else:
            while column_counter <= grid_size:
                emoji_output += BLUE_BOX
                column_counter += 1
        row_counter += 1
        print(emoji_output)
        

def correct_guess(secret_row: int, secret_column: int, guess_row: int, guess_column: int) -> bool:
    """Determine if a guess is correct or not."""
    if guess_row == secret_row and guess_column == secret_column:
        return True
    else:
        return False


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Main code of program."""
    user_turn: int = 1
    while user_turn <= 5:
        print(f"=== Turn {user_turn}/5 ===")
        guess_row: int = input_guess(grid_size, "row")
        guess_column: int = input_guess(grid_size, "column")
        correctness: bool = correct_guess(secret_row, secret_column, guess_row, guess_column)
        print_grid(grid_size, guess_row, guess_column, correctness)
        if correctness:
            print("Hit!")
            print(f"You won in {user_turn}/5 turns!")
            user_turn += 5
        else: 
            print("Miss!")
            if user_turn >= 5:
                print("X/5 - Better luck next time!")
        user_turn += 1
  

if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))