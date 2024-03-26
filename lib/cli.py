# lib/cli.py


# from models.questions import Questions
# from models.player import Player


from helpers import (
    exit_program,
    helper_1,
    add_question,
    start_new_game,
    is_new_high_score,
    minimum_high_score,
    add_player_to_high_scores,
    see_all_questions,
    delete_question,
    delete_high_score,
    update_question
)



def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            start_new_game()
        elif choice == "2":
            is_new_high_score()
        # elif choice == "7":
        #     this_wont_work()
        
        # elif choice == "3":
        #     minimum_high_score()
        # elif choice == "4":
        #     add_question()
        # elif choice == "5":
        #     see_all_questions()
        # elif choice == "6":
        #     delete_question()
        # elif choice == "7":
        #     delete_high_score()
        # elif choice == "8":
        #     update_question()
        elif choice == "9":
            admin_menu()
            y = True
            while (y):
                choice = input("> ")
                if choice == "0":
                    y = False
                elif choice == "3":
                    minimum_high_score()
                    y = False
                elif choice == "4":
                    add_question()
                    y = False
                elif choice == "5":
                    see_all_questions()
                    y = False
                elif choice == "6":
                    delete_question()
                    y = False
                elif choice == "7":
                    delete_high_score()
                    y = False
                elif choice == "8":
                    update_question()
                    y = False


        else:
            print("Invalid choice")


def menu():
    # print(
    #     """ 
    # Admin Only Tasks:
    #     3. Show Lowest High Score
    #     4. Add Question
    #     5. See All Questions
    #     6. Delete A Question
    #     7. Delete A High Score
    #     8. Update Question
    # """)

    print("\nPlease select an option:")
    print("0. Exit the Program")
    print("1. Start New Game")
    print("2. Get High Scores\n")
    print("9. Admin Menu")
    # print("4. Add Question")
    # print("5. See All Questions")
    # print("6. Delete A Question")
    # print("7. Delete A High Score")
    # print("8. Update Question")

def admin_menu():
    print(
    """ 
    Admin Only Tasks:
        3. Show Lowest High Score
        4. Add Question
        5. See All Questions
        6. Delete A Question
        7. Delete A High Score
        8. Update Question
        0. Exit to Main Menu
    """)



if __name__ == "__main__":
    main()
