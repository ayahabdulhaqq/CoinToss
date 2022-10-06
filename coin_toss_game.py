"""Coin Toss Game!"""

__author__ = "Ayah Abdul-Haqq"


points: int = 4
player: str = ""
SAD_FACE: str = "\U0001F615"
CELEBRATE_FACE: str = "\U0001F600"


def main() -> None:
    """Game entrypoint."""
    global player
    while player == "":
        greet()
    option: str = input(f"Hey there, {player}! Would you like to 1. play, 2. learn more about the game, or 3. exit? ")
    if option == "1":
        game: bool = True
        user: bool = True
        global points
        global CELEBRATE_FACE
        turns: int = 0
        while game and user:
            from random import randint

            print(f"|| Points: {points} ||")
            while turns < 10 and points != 0:
                heads_or_tails: int = randint(1, 2)
                answer: int = int(input(f"{player}, 1. Heads or 2. Tails?: "))
                if answer == heads_or_tails:
                    print(f"You got it, {player}!{CELEBRATE_FACE}")
                    points += 1
                    turns += 1
                if answer != heads_or_tails:
                    print(f"Sorry {player}, you got it wrong.{SAD_FACE}")
                    points += 1
                    turns += 1
            while turns < 10 and points == 0:
                print("Good try. Better luck next time!")
                exit()
            while turns == 10 and points > 0:
                answer = int(input(f"Good job! You finished the game with {points} points! Would you like to 1. play again, or 2. exit? "))
                if answer == 1:
                    main()
                if answer == 2:
                    leave()
    if option == "2":
        learn_more()
    if option == "3":
        leave()


def greet() -> None:
    """Greets the player."""
    global player
    print("Hello! Welcome to the cointoss game!")
    player = input("What is your name? ")

        
def learn_more() -> None:
    """Learn more about the game."""
    option: str = input("Great! Cointoss is a game where you guess heads or tails and see if you guess correctly or not!\nYou have 10 tries, and start with 4 points. When you guess correctly, you get 1 point, and when you guess incorrectly, you lose a point. The game ends once you have 0 points or once you have used all your tries.\nWould you like to 1. play, or 2. exit? ")
    if option == "1":
        main()
    if option == "2":
        leave()


def leave() -> None:
    """Exits the game."""
    global SAD_FACE

    print(f"Come play soon {SAD_FACE}! You left the game with {points} points.")
    exit()


if __name__ == "__main__":
    main()