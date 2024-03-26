# lib/helpers.py


from models.questions import Questions
from models.player import Player



def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()



# def ex():
#     print(f'Question {question_level_current}:    {current_question.text}\n')
#     print(f'\ta) \t{current_question.correct_answer}')
#     print(f'\tb) \t{current_question.w_answer1}')
#     print(f'\tc) \t{current_question.w_answer2}')
#     print(f'\td) \t{current_question.w_answer3}')



    # try:
    #     user_input = input("Please type the letter of your answer choice\n")
    #     if(user_input == 'a'):
    #         print("correct")
    #         break
    #     elif(user_input == 'b'):
    #         print("incorrect answer b")
    #         break
    #     elif(user_input == 'c'):
    #         print("incorrect answer c")
    #         break
    #     elif(user_input == 'd'):
    #         print("incorrect answer d") 
    #         break
    #     else:
    #         print("Please try again a,b,c,d")
    # except:
    #     pass


# def answer_choices (question_level_current, next_function):
#     question_list = Questions.find_by_level(question_level_current)
#     index_value = 0
#     current_question = question_list[index_value]

#     x = True
#     while(x):
#         print(f'Level {question_level_current}\n\n')
#         question_output(current_question, question_level_current)
#         try:
#             user_input = input("Please type the letter of your answer choice\n")
#             if(user_input == 'a'):
#                 print("correct")
#                 new_level = question_level_current + 1
#                 next_function(new_level)


#             elif(user_input == 'b'):
#                 print("incorrect answer b")
#                 x = False
#             elif(user_input == 'c'):
#                 print("incorrect answer c")
#                 x = False
#             elif(user_input == 'd'):
#                 print("incorrect answer d") 
#                 x = False
#             else:
#                 print("Please try again a,b,c,d")
#         except:
#             print("Invalid input! Please try again!\n")








def start_new_game():
    player_name = input("\nPlease type the name of the player: ")
    q_level = 0
    current_score = 0

    player1 = Player.create(player_name, q_level, current_score)

    current_score = player1.current_score


    question_level_current = 1
    question_list = Questions.find_by_level(question_level_current)
    index_value = 0
    current_question = question_list[index_value]
        # game_running(1, current_question)

    x = True
    while(x):
        print(f'Level {question_level_current}\n\n')
        question_output_BBB(current_question, question_level_current)
        try:
            user_input = input("Please type the letter of your answer choice\n")
            if(user_input == 'b'):
                print("correct")
                current_score += 100
# _______________________________________-
                question_level_current = 2
                question_list = Questions.find_by_level(question_level_current)
                index_value = 0
                current_question = question_list[index_value]
                    # game_running(1, current_question)
                while(x):
                    print(f'Level {question_level_current}\n\n')
                    question_output_AAA(current_question, question_level_current)
                    try:
                        user_input = input("Please type the letter of your answer choice\n")
                        if(user_input == 'a'):
                            print("correct")
                            current_score += 100
                            # _______________________________
                            question_level_current = 3
                            question_list = Questions.find_by_level(question_level_current)
                            index_value = 0
                            current_question = question_list[index_value]
                                # game_running(1, current_question)
                            while(x):
                                print(f'Level {question_level_current}\n\n')
                                question_output_CCC(current_question, question_level_current)
                                try:
                                    user_input = input("Please type the letter of your answer choice\n")
                                    if(user_input == 'c'):
                                        print("correct")
                                        current_score += 100
                                        print('You Win The Game, Congratulations')
                                        print(f'Score: {current_score}')
                                        x = False
                                        # _______________________________
                                        # question_level_current = 4
                                        # question_list = Questions.find_by_level(question_level_current)
                                        # index_value = 0
                                        # current_question = question_list[index_value]
                                        #     # game_running(1, current_question)
                                        # while(x):
                                        #     print(f'Level {question_level_current}\n\n')
                                        #     question_output_CCC(current_question, question_level_current)
                                        #     try:
                                        #         user_input = input("Please type the letter of your answer choice\n")
                                        #         if(user_input == 'c'):
                                        #             print("correct")
                                        #             # _______________________________
                                        #             question_level_current = 5
                                        #             question_list = Questions.find_by_level(question_level_current)
                                        #             index_value = 0
                                        #             current_question = question_list[index_value]
                                        #                 # game_running(1, current_question)
                                        #             while(x):
                                        #                 print(f'Level {question_level_current}\n\n')
                                        #                 question_output_CCC(current_question, question_level_current)
                                        #                 try:
                                        #                     user_input = input("Please type the letter of your answer choice\n")
                                        #                     if(user_input == 'c'):
                                        #                         print("correct")
                                        #                         # _______________________________
                                        #                         question_level_current = 6
                                        #                         question_list = Questions.find_by_level(question_level_current)
                                        #                         index_value = 0
                                        #                         current_question = question_list[index_value]
                                        #                             # game_running(1, current_question)
                                        #                         while(x):
                                        #                             print(f'Level {question_level_current}\n\n')
                                        #                             question_output_CCC(current_question, question_level_current)
                                        #                             try:
                                        #                                 user_input = input("Please type the letter of your answer choice\n")
                                        #                                 if(user_input == 'c'):
                                        #                                     print("correct")
                                        #                                     # _______________________________
                                        #                                     question_level_current = 7
                                        #                                     question_list = Questions.find_by_level(question_level_current)
                                        #                                     index_value = 0
                                        #                                     current_question = question_list[index_value]
                                        #                                         # game_running(1, current_question)
                                        #                                     while(x):
                                        #                                         print(f'Level {question_level_current}\n\n')
                                        #                                         question_output_CCC(current_question, question_level_current)
                                        #                                         try:
                                        #                                             user_input = input("Please type the letter of your answer choice\n")
                                        #                                             if(user_input == 'c'):
                                        #                                                 print("correct")
                                        #                                                 # _______________________________
                                        #                                                 question_level_current = 8
                                        #                                                 question_list = Questions.find_by_level(question_level_current)
                                        #                                                 index_value = 0
                                        #                                                 current_question = question_list[index_value]
                                        #                                                     # game_running(1, current_question)
                                        #                                                 while(x):
                                        #                                                     print(f'Level {question_level_current}\n\n')
                                        #                                                     question_output_CCC(current_question, question_level_current)
                                        #                                                     try:
                                        #                                                         user_input = input("Please type the letter of your answer choice\n")
                                        #                                                         if(user_input == 'c'):
                                        #                                                             print("correct")
                                        #                                                             # _______________________________
                                        #                                                             question_level_current = 9
                                        #                                                             question_list = Questions.find_by_level(question_level_current)
                                        #                                                             index_value = 0
                                        #                                                             current_question = question_list[index_value]
                                        #                                                                 # game_running(1, current_question)
                                        #                                                             while(x):
                                        #                                                                 print(f'Level {question_level_current}\n\n')
                                        #                                                                 question_output_CCC(current_question, question_level_current)
                                        #                                                                 try:
                                        #                                                                     user_input = input("Please type the letter of your answer choice\n")
                                        #                                                                     if(user_input == 'c'):
                                        #                                                                         print("correct")
                                        #                                                                         # _______________________________
                                        #                                                                         question_level_current = 10
                                        #                                                                         question_list = Questions.find_by_level(question_level_current)
                                        #                                                                         index_value = 0
                                        #                                                                         current_question = question_list[index_value]
                                        #                                                                             # game_running(1, current_question)
                                        #                                                                         while(x):
                                        #                                                                             print(f'Level {question_level_current}\n\n')
                                        #                                                                             question_output_CCC(current_question, question_level_current)
                                        #                                                                             try:
                                        #                                                                                 user_input = input("Please type the letter of your answer choice\n")
                                        #                                                                                 if(user_input == 'c'):
                                        #                                                                                     print("correct")
                                        #                                                                                     print("YOU WIN YAYYYYYY")
                                        #                                                                                     x = False
                                        #                                                                                     # _______________________________


                                        #                                                                                     # _______________________________
                                                                                                                            
                                        #                                                                                 elif(user_input == 'b'):
                                        #                                                                                     print("incorrect answer b")
                                        #                                                                                     x = False
                                        #                                                                                 elif(user_input == 'a'):
                                        #                                                                                     print("incorrect answer a")
                                        #                                                                                     x = False
                                        #                                                                                 elif(user_input == 'd'):
                                        #                                                                                     print("incorrect answer d") 
                                        #                                                                                     x = False
                                        #                                                                                 else:
                                        #                                                                                     print("Please try again a,b,c,d")
                                        #                                                                             except:
                                        #                                                                                 print("Invalid input! Please try again!\n")

                                        #                                                                         # _______________________________
                                                                                                                
                                        #                                                                     elif(user_input == 'b'):
                                        #                                                                         print("incorrect answer b")
                                        #                                                                         x = False
                                        #                                                                     elif(user_input == 'a'):
                                        #                                                                         print("incorrect answer a")
                                        #                                                                         x = False
                                        #                                                                     elif(user_input == 'd'):
                                        #                                                                         print("incorrect answer d") 
                                        #                                                                         x = False
                                        #                                                                     else:
                                        #                                                                         print("Please try again a,b,c,d")
                                        #                                                                 except:
                                        #                                                                     print("Invalid input! Please try again!\n")

                                        #                                                             # _______________________________
                                                                                                    
                                        #                                                         elif(user_input == 'b'):
                                        #                                                             print("incorrect answer b")
                                        #                                                             x = False
                                        #                                                         elif(user_input == 'a'):
                                        #                                                             print("incorrect answer a")
                                        #                                                             x = False
                                        #                                                         elif(user_input == 'd'):
                                        #                                                             print("incorrect answer d") 
                                        #                                                             x = False
                                        #                                                         else:
                                        #                                                             print("Please try again a,b,c,d")
                                        #                                                     except:
                                        #                                                         print("Invalid input! Please try again!\n")

                                        #                                                 # _______________________________
                                                                                        
                                        #                                             elif(user_input == 'b'):
                                        #                                                 print("incorrect answer b")
                                        #                                                 x = False
                                        #                                             elif(user_input == 'a'):
                                        #                                                 print("incorrect answer a")
                                        #                                                 x = False
                                        #                                             elif(user_input == 'd'):
                                        #                                                 print("incorrect answer d") 
                                        #                                                 x = False
                                        #                                             else:
                                        #                                                 print("Please try again a,b,c,d")
                                        #                                         except:
                                        #                                             print("Invalid input! Please try again!\n")

                                        #                                     # _______________________________
                                                                            
                                        #                                 elif(user_input == 'b'):
                                        #                                     print("incorrect answer b")
                                        #                                     x = False
                                        #                                 elif(user_input == 'a'):
                                        #                                     print("incorrect answer a")
                                        #                                     x = False
                                        #                                 elif(user_input == 'd'):
                                        #                                     print("incorrect answer d") 
                                        #                                     x = False
                                        #                                 else:
                                        #                                     print("Please try again a,b,c,d")
                                        #                             except:
                                        #                                 print("Invalid input! Please try again!\n")

                                        #                         # _______________________________
                                                                
                                        #                     elif(user_input == 'b'):
                                        #                         print("incorrect answer b")
                                        #                         x = False
                                        #                     elif(user_input == 'a'):
                                        #                         print("incorrect answer a")
                                        #                         x = False
                                        #                     elif(user_input == 'd'):
                                        #                         print("incorrect answer d") 
                                        #                         x = False
                                        #                     else:
                                        #                         print("Please try again a,b,c,d")
                                        #                 except:
                                        #                     print("Invalid input! Please try again!\n")

                                        #             # _______________________________
                                                    
                                        #         elif(user_input == 'b'):
                                        #             print("incorrect answer b")
                                        #             x = False
                                        #         elif(user_input == 'a'):
                                        #             print("incorrect answer a")
                                        #             x = False
                                        #         elif(user_input == 'd'):
                                        #             print("incorrect answer d") 
                                        #             x = False
                                        #         else:
                                        #             print("Please try again a,b,c,d")
                                        #     except:
                                        #         print("Invalid input! Please try again!\n")

                                        # _______________________________
                                        
                                    elif(user_input == 'b'):
                                        print("incorrect answer b")
                                        player1.current_score = current_score
                                        player1.update()
                                        print(f'Score: {player1.current_score}\n')
                                        x = False
                                    elif(user_input == 'a'):
                                        print("incorrect answer a")
                                        player1.current_score = current_score
                                        player1.update()
                                        print(f'Score: {player1.current_score}\n')
                                        x = False
                                    elif(user_input == 'd'):
                                        print("incorrect answer d") 
                                        player1.current_score = current_score
                                        player1.update()
                                        print(f'Score: {player1.current_score}\n')
                                        x = False
                                    else:
                                        print("Please try again a,b,c,d")
                                except:
                                    print("Invalid input! Please try again!\n")


                            # _______________________________
                            
                        elif(user_input == 'b'):
                            print("incorrect answer b")
                            player1.current_score = current_score
                            player1.update()
                            print(f'Score: {current_score}\n')
                            x = False
                        elif(user_input == 'c'):
                            print("incorrect answer c")
                            player1.current_score = current_score
                            player1.update()
                            print(f'Score: {current_score}\n')
                            x = False
                        elif(user_input == 'd'):
                            print("incorrect answer d") 
                            player1.current_score = current_score
                            player1.update()
                            print(f'Score: {current_score}\n')
                            x = False
                        else:
                            print("Please try again a,b,c,d")
                    except:
                        print("Invalid input! Please try again!\n")
# ________________________________________


            elif(user_input == 'a'):
                print("incorrect answer a")
                player1.current_score = current_score
                player1.update()
                print(f'Score: {current_score}\n')
                x = False
            elif(user_input == 'c'):
                print("incorrect answer c")
                player1.current_score = current_score
                player1.update()
                print(f'Score: {current_score}\n')
                x = False
            elif(user_input == 'd'):
                print("incorrect answer d") 
                player1.current_score = current_score
                player1.update()
                print(f'Score: {current_score}\n')
                x = False
            else:
                print("Please try again a,b,c,d")
        except:
            print("Invalid input! Please try again!\n")



    # How we can add teh high scores table in there___________
    # if(player1.current_score > high_score):
        # update the high score table
    





def question_output_AAA(current_question, question_level_current):
    print(f'Question {question_level_current}:    {current_question.text}\n')
    print(f'\ta) \t{current_question.correct_answer}')
    print(f'\tb) \t{current_question.w_answer1}')
    print(f'\tc) \t{current_question.w_answer2}')
    print(f'\td) \t{current_question.w_answer3}')

def question_output_BBB(current_question, question_level_current):
    print(f'Question {question_level_current}:    {current_question.text}\n')
    print(f'\ta) \t{current_question.w_answer1}')
    print(f'\tb) \t{current_question.correct_answer}')
    print(f'\tc) \t{current_question.w_answer2}')
    print(f'\td) \t{current_question.w_answer3}')

def question_output_CCC(current_question, question_level_current):
    print(f'Question {question_level_current}:    {current_question.text}\n')
    print(f'\ta) \t{current_question.w_answer1}')
    print(f'\tb) \t{current_question.w_answer2}')
    print(f'\tc) \t{current_question.correct_answer}')
    print(f'\td) \t{current_question.w_answer3}')

def question_output_DDD(current_question, question_level_current):
    print(f'Question {question_level_current}:    {current_question.text}\n')
    print(f'\ta) \t{current_question.w_answer1}')
    print(f'\tb) \t{current_question.w_answer2}')
    print(f'\tc) \t{current_question.w_answer3}')
    print(f'\td) \t{current_question.correct_answer}')




# def game_running(question_level_current, current_question):
#     answer_was_correct = ""
#     while(True):
#         # question_level_current = 1
#         print(f'Level {question_level_current}\n\n')

#         # question_list = Questions.find_by_level(question_level_current)
#         # index_value = 0
#         # current_question = question_list[index_value]

#         question_output(current_question, question_level_current)


#         try:
#             user_input = input("Please type the letter of your answer choice\n")
#             if(user_input == 'a'):
#                 print("correct")
#                 answer_was_correct = "correct"
#                 break
#             elif(user_input == 'b'):
#                 print("incorrect answer b")
#                 answer_was_correct = "incorrect"
#                 break
#             elif(user_input == 'c'):
#                 print("incorrect answer c")
#                 answer_was_correct = "incorrect"
#                 break
#             elif(user_input == 'd'):
#                 print("incorrect answer d")
#                 answer_was_correct = "incorrect"
#                 break
#             else:
#                 print("Please try again a,b,c,d")
#         except:
#             print("Invalid input! Please try again!\n")
    
#     return answer_was_correct













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

