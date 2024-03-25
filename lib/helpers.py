# lib/helpers.py


from models.questions import Questions
from models.player import Player



def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()



def start_new_game():
    # player_name = input("\nPlease type the name of the player: ")
    # q_level = 0
    # current_score = 0

    # Player.create(player_name, q_level, current_score)

    while(True):
        question_level_current = 1
        print(f'Level {question_level_current}\n\n')

        question_list = Questions.find_by_level(question_level_current)
        index_value = 1
        current_question = question_list[index_value]

        print(f'Question {question_level_current}:    {current_question.text}\n')
        print(f'\ta) \t{current_question.correct_answer}')
        print(f'\tb) \t{current_question.w_answer1}')
        print(f'\tc) \t{current_question.w_answer2}')
        print(f'\td) \t{current_question.w_answer3}')


        try:
            user_input = input("Please type the letter of your answer choice\n")
            if(user_input == 'a'):
                print("correct")
                break
            elif(user_input == 'b'):
                print("incorrect answer b")
                break
            elif(user_input == 'c'):
                print("incorrect answer c")
                break
            elif(user_input == 'd'):
                print("incorrect answer d") 
                break
            else:
                print("Please try again a,b,c,d")
        except:
            print("Invalid input! Please try again!\n")

















def add_question():
    q_level = input("\nPlease enter the level of your new question: ")
    q_level = int(q_level)

    q_text = input("\nPlease enter the question text: ")
    q_correct_answer = input("\nPlease enter the correct answer to your question: ")
    q_w_answer1 = input("\nPlease enter the first wrong answer choice: ")
    q_w_answer2 = input("\nPlease enter the second wrong answer choice: ")
    q_w_answer3 = input("\nPlease enter the third wrong answer choice: ")

    new_question = Questions.create(q_level, q_text, q_correct_answer, q_w_answer1, q_w_answer2, q_w_answer3)
    print("Here is the information for the new question:")
    print(new_question)





    # print(f'Your question is {q_text} and is a level {q_level} question')

