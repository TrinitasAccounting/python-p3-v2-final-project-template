# lib/cli.py


# from models.questions import Questions
# from models.player import Player


from helpers import (
    exit_program,
    helper_1,
    add_question,
    start_new_game
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            start_new_game()
        elif choice == "4":
            add_question()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Start a new game")
    print("4. Add Question")


if __name__ == "__main__":
    main()
