# lib/helpers.py


from random import randrange

from models.questions import Questions
from models.player import Player
from models.high_scores import High_Scores



def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()



# Attempted to make the nested questions into a loop, but could not figure it out___________

# def new_game_test(question_level,letters, correct):

#     question_level_current = question_level
#     # player1.question_level = question_level
#     question_list = Questions.find_by_level(question_level_current)
#     length = len(question_list)
#     index_value = randrange(0,length)
#     current_question = question_list[index_value]

#     x = True
#     while(x):
#         print(f'Level {question_level_current}\n\n')
#         if(letters == "BBB"):
#             question_output_BBB(current_question, question_level_current)
#         elif(letters == "AAA"):
#             question_output_AAA(current_question, question_level_current)
#         elif(letters == "CCC"):
#             question_output_CCC(current_question, question_level_current)
#         elif(letters == "DDD"):
#             question_output_DDD(current_question, question_level_current)
#         else:
#             print("what the heck just happened")

#         user_input = input("Please type the letter of your answer choice: ")
#         if(letters == "BBB"):
#             if(user_input == 'b'):
#                 current_score_new += 100
#                 question_level = question_level + 1
#                 y = new_game_test
#                 if(question_level == 10):
#                     # x = exit_program()
#                     x = False
#                 else:
#                     y = new_game_test

#                 letters_next = "BBB"
#                 # letters_value = randrange(1,4)

#                 # if (letters_value == 1):
#                 #     letters_next = "AAA" 
#                 # elif(letters_value == 2):
#                 #     letters_next = "BBB"
#                 # elif(letters_value == 3):
#                 #     letters_next = "CCC"
#                 # elif(letters_value == 4):
#                 #     letters_next = "DDD"
#                 correct(question_level, letters_next, y)
#             elif(user_input == 'a'):
#                 print("incorrect answer a")
#                 player1.current_score = current_score
#                 player1.update()
#                 print(f'Score: {current_score}\n')
#                 add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
#                 x = False
#             elif(user_input == 'c'):
#                 print("incorrect answer c")
#                 player1.current_score = current_score
#                 player1.update()
#                 print(f'Score: {current_score}\n')
#                 add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
#                 x = False
#             elif(user_input == 'd'):
#                 print("incorrect answer d")
#                 player1.current_score = current_score
#                 player1.update()
#                 print(f'Score: {current_score}\n')
#                 add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
#                 x = False


# def this_wont_work():
#     player_name = input("\nPlease type the name of the player: ")
#     q_level = 1
#     current_score = 0

#     player1 = Player.create(player_name, q_level, current_score)

#     current_score = player1.current_score

#     current_score_new = 0

#     new_game_test(1, "BBB", new_game_test)








def start_new_game():

    # Creating the initial player build____________________________________
    player_name = input("\nPlease type the name of the player: ")
    q_level = 1
    current_score = 0

    player1 = Player.create(player_name, q_level, current_score)

    current_score = player1.current_score

    # This is where the questions looping begins__________________________________
    question_level_current = 1
    player1.question_level = question_level_current
    question_list = Questions.find_by_level(question_level_current)
    length = len(question_list)
    index_value = randrange(0,length)
    current_question = question_list[index_value]
        # game_running(1, current_question)

    x = True
    while(x):
        print(f'Level {question_level_current}\n\n')
        question_output_BBB(current_question, question_level_current)
        try:
            user_input = input("Please type the letter of your answer choice\n")
            if(user_input == 'b'):
                print("\n\nCorrect!!!!!!\n\n")
                current_score += 100
# _______________________________________-
                question_level_current = 2
                player1.question_level = question_level_current
                question_list = Questions.find_by_level(question_level_current)
                length = len(question_list)
                index_value = randrange(0,length)
                current_question = question_list[index_value]
                    # game_running(1, current_question)
                while(x):
                    print(f'Level {question_level_current}\n\n')
                    question_output_AAA(current_question, question_level_current)
                    try:
                        user_input = input("Please type the letter of your answer choice\n")
                        if(user_input == 'a'):
                            print("\n\nCorrect!!!!!!\n\n")
                            current_score += 100
                            # _______________________________
                            question_level_current = 3
                            player1.question_level = question_level_current
                            question_list = Questions.find_by_level(question_level_current)
                            length = len(question_list)
                            index_value = randrange(0,length)
                            current_question = question_list[index_value]
                                # game_running(1, current_question)
                            while(x):
                                print(f'Level {question_level_current}\n\n')
                                question_output_CCC(current_question, question_level_current)
                                try:
                                    user_input = input("Please type the letter of your answer choice\n")
                                    if(user_input == 'c'):
                                        print("\n\nCorrect!!!!!!\n\n")
                                        current_score += 100
                                        # _______________________________
                                        question_level_current = 4
                                        player1.question_level = question_level_current
                                        question_list = Questions.find_by_level(question_level_current)
                                        length = len(question_list)
                                        index_value = randrange(0,length)
                                        current_question = question_list[index_value]
                                            # game_running(1, current_question)
                                        while(x):
                                            print(f'Level {question_level_current}\n\n')
                                            question_output_BBB(current_question, question_level_current)
                                            try:
                                                user_input = input("Please type the letter of your answer choice\n")
                                                if(user_input == 'b'):
                                                    print("\n\nCorrect!!!!!!\n\n")
                                                    current_score += 100
                                                    # _______________________________
                                                    question_level_current = 5
                                                    player1.question_level = question_level_current
                                                    question_list = Questions.find_by_level(question_level_current)
                                                    length = len(question_list)
                                                    index_value = randrange(0,length)
                                                    current_question = question_list[index_value]
                                                        # game_running(1, current_question)
                                                    while(x):
                                                        print(f'Level {question_level_current}\n\n')
                                                        question_output_DDD(current_question, question_level_current)
                                                        try:
                                                            user_input = input("Please type the letter of your answer choice\n")
                                                            if(user_input == 'd'):
                                                                print("\n\nCorrect!!!!!!\n\n")
                                                                current_score += 100
                                                                # _______________________________
                                                                question_level_current = 6
                                                                player1.question_level = question_level_current
                                                                question_list = Questions.find_by_level(question_level_current)
                                                                length = len(question_list)
                                                                index_value = randrange(0,length)
                                                                current_question = question_list[index_value]
                                                                    # game_running(1, current_question)
                                                                while(x):
                                                                    print(f'Level {question_level_current}\n\n')
                                                                    question_output_DDD(current_question, question_level_current)
                                                                    try:
                                                                        user_input = input("Please type the letter of your answer choice\n")
                                                                        if(user_input == 'd'):
                                                                            print("\n\nCorrect!!!!!!\n\n")
                                                                            current_score += 100
                                                                            # _______________________________
                                                                            question_level_current = 7
                                                                            player1.question_level = question_level_current
                                                                            question_list = Questions.find_by_level(question_level_current)
                                                                            length = len(question_list)
                                                                            index_value = randrange(0,length)
                                                                            current_question = question_list[index_value]
                                                                                # game_running(1, current_question)
                                                                            while(x):
                                                                                print(f'Level {question_level_current}\n\n')
                                                                                question_output_AAA(current_question, question_level_current)
                                                                                try:
                                                                                    user_input = input("Please type the letter of your answer choice\n")
                                                                                    if(user_input == 'a'):
                                                                                        print("\n\nCorrect!!!!!!\n\n")
                                                                                        current_score += 100
                                                                                        # _______________________________
                                                                                        question_level_current = 8
                                                                                        player1.question_level = question_level_current
                                                                                        question_list = Questions.find_by_level(question_level_current)
                                                                                        length = len(question_list)
                                                                                        index_value = randrange(0,length)
                                                                                        current_question = question_list[index_value]
                                                                                            # game_running(1, current_question)
                                                                                        while(x):
                                                                                            print(f'Level {question_level_current}\n\n')
                                                                                            question_output_CCC(current_question, question_level_current)
                                                                                            try:
                                                                                                user_input = input("Please type the letter of your answer choice\n")
                                                                                                if(user_input == 'c'):
                                                                                                    print("\n\nCorrect!!!!!!\n\n")
                                                                                                    current_score += 100
                                                                                                    # _______________________________
                                                                                                    question_level_current = 9
                                                                                                    player1.question_level = question_level_current
                                                                                                    question_list = Questions.find_by_level(question_level_current)
                                                                                                    length = len(question_list)
                                                                                                    index_value = randrange(0,length)
                                                                                                    current_question = question_list[index_value]
                                                                                                        # game_running(1, current_question)
                                                                                                    while(x):
                                                                                                        print(f'Level {question_level_current}\n\n')
                                                                                                        question_output_AAA(current_question, question_level_current)
                                                                                                        try:
                                                                                                            user_input = input("Please type the letter of your answer choice\n")
                                                                                                            if(user_input == 'a'):
                                                                                                                print("\n\nCorrect!!!!!!\n\n")
                                                                                                                current_score += 100
                                                                                                                # _______________________________
                                                                                                                question_level_current = 10
                                                                                                                player1.question_level = question_level_current
                                                                                                                question_list = Questions.find_by_level(question_level_current)
                                                                                                                length = len(question_list)
                                                                                                                index_value = randrange(0,length)
                                                                                                                current_question = question_list[index_value]
                                                                                                                    # game_running(1, current_question)
                                                                                                                while(x):
                                                                                                                    print(f'Level {question_level_current}\n\n')
                                                                                                                    question_output_BBB(current_question, question_level_current)
                                                                                                                    try:
                                                                                                                        user_input = input("Please type the letter of your answer choice\n")
                                                                                                                        if(user_input == 'b'):
                                                                                                                            print("\n\nCorrect!!!!!!\n\n")
                                                                                                                            current_score += 100
                                                                                                                            player1.current_score = current_score
                                                                                                                            player1.update()
                                                                                                                            add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                                                                                                            print('____________________________________________________')
                                                                                                                            print('You Win The Game, Congratulations')
                                                                                                                            print(f'Score: {current_score}')
                                                                                                                            print('____________________________________________________')
                                                                                                                            x = False
                                                                                                                            # _______________________________

                                                                                                                            # _______________________________
                                                                                                                            
                                                                                                                        elif(user_input == 'a'):
                                                                                                                            print("\n")
                                                                                                                            print("incorrect answer a")
                                                                                                                            print("\n")
                                                                                                                            player1.current_score = current_score
                                                                                                                            player1.update()
                                                                                                                            print(f'Score: {player1.current_score}\n')
                                                                                                                            add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                                                                                                            x = False
                                                                                                                        elif(user_input == 'c'):
                                                                                                                            print("\n")
                                                                                                                            print("incorrect answer c")
                                                                                                                            print("\n")
                                                                                                                            player1.current_score = current_score
                                                                                                                            player1.update()
                                                                                                                            print(f'Score: {player1.current_score}\n')
                                                                                                                            add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                                                                                                            x = False
                                                                                                                        elif(user_input == 'd'):
                                                                                                                            print("\n")
                                                                                                                            print("incorrect answer d") 
                                                                                                                            print("\n")
                                                                                                                            player1.current_score = current_score
                                                                                                                            player1.update()
                                                                                                                            print(f'Score: {player1.current_score}\n')
                                                                                                                            add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                                                                                                            x = False
                                                                                                                        else:
                                                                                                                            print("Please try again a,b,c,d")
                                                                                                                    except:
                                                                                                                        print("Invalid input! Please try again!\n")

                                                                                                                # _______________________________
                                                                                                                
                                                                                                            elif(user_input == 'b'):
                                                                                                                print("\n")
                                                                                                                print("incorrect answer b")
                                                                                                                print("\n")
                                                                                                                player1.current_score = current_score
                                                                                                                player1.update()
                                                                                                                print(f'Score: {player1.current_score}\n')
                                                                                                                add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                                                                                                x = False
                                                                                                            elif(user_input == 'c'):
                                                                                                                print("\n")
                                                                                                                print("incorrect answer c")
                                                                                                                print("\n")
                                                                                                                player1.current_score = current_score
                                                                                                                player1.update()
                                                                                                                print(f'Score: {player1.current_score}\n')
                                                                                                                add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                                                                                                x = False
                                                                                                            elif(user_input == 'd'):
                                                                                                                print("\n")
                                                                                                                print("incorrect answer d") 
                                                                                                                print("\n")
                                                                                                                player1.current_score = current_score
                                                                                                                player1.update()
                                                                                                                print(f'Score: {player1.current_score}\n')
                                                                                                                add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                                                                                                x = False
                                                                                                            else:
                                                                                                                print("Please try again a,b,c,d")
                                                                                                        except:
                                                                                                            print("Invalid input! Please try again!\n")

                                                                                                    # _______________________________
                                                                                                    
                                                                                                elif(user_input == 'b'):
                                                                                                    print("\n")
                                                                                                    print("incorrect answer b")
                                                                                                    print("\n")
                                                                                                    player1.current_score = current_score
                                                                                                    player1.update()
                                                                                                    print(f'Score: {player1.current_score}\n')
                                                                                                    add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                                                                                    x = False
                                                                                                elif(user_input == 'a'):
                                                                                                    print("\n")
                                                                                                    print("incorrect answer a")
                                                                                                    print("\n")
                                                                                                    player1.current_score = current_score
                                                                                                    player1.update()
                                                                                                    print(f'Score: {player1.current_score}\n')
                                                                                                    add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                                                                                    x = False
                                                                                                elif(user_input == 'd'):
                                                                                                    print("\n")
                                                                                                    print("incorrect answer d") 
                                                                                                    print("\n")
                                                                                                    player1.current_score = current_score
                                                                                                    player1.update()
                                                                                                    print(f'Score: {player1.current_score}\n')
                                                                                                    add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                                                                                    x = False
                                                                                                else:
                                                                                                    print("Please try again a,b,c,d")
                                                                                            except:
                                                                                                print("Invalid input! Please try again!\n")

                                                                                        # _______________________________
                                                                                        
                                                                                    elif(user_input == 'b'):
                                                                                        print("\n")
                                                                                        print("incorrect answer b")
                                                                                        print("\n")
                                                                                        player1.current_score = current_score
                                                                                        player1.update()
                                                                                        print(f'Score: {player1.current_score}\n')
                                                                                        add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                                                                        x = False
                                                                                    elif(user_input == 'c'):
                                                                                        print("\n")
                                                                                        print("incorrect answer c")
                                                                                        print("\n")
                                                                                        player1.current_score = current_score
                                                                                        player1.update()
                                                                                        print(f'Score: {player1.current_score}\n')
                                                                                        add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                                                                        x = False
                                                                                    elif(user_input == 'd'):
                                                                                        print("\n")
                                                                                        print("incorrect answer d") 
                                                                                        print("\n")
                                                                                        player1.current_score = current_score
                                                                                        player1.update()
                                                                                        print(f'Score: {player1.current_score}\n')
                                                                                        add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                                                                        x = False
                                                                                    else:
                                                                                        print("Please try again a,b,c,d")
                                                                                except:
                                                                                    print("Invalid input! Please try again!\n")

                                                                            # _______________________________
                                                                            
                                                                        elif(user_input == 'b'):
                                                                            print("\n")
                                                                            print("incorrect answer b")
                                                                            print("\n")
                                                                            player1.current_score = current_score
                                                                            player1.update()
                                                                            print(f'Score: {player1.current_score}\n')
                                                                            add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                                                            x = False
                                                                        elif(user_input == 'a'):
                                                                            print("\n")
                                                                            print("incorrect answer a")
                                                                            print("\n")
                                                                            player1.current_score = current_score
                                                                            player1.update()
                                                                            print(f'Score: {player1.current_score}\n')
                                                                            add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                                                            x = False
                                                                        elif(user_input == 'c'):
                                                                            print("\n")
                                                                            print("incorrect answer c") 
                                                                            print("\n")
                                                                            player1.current_score = current_score
                                                                            player1.update()
                                                                            print(f'Score: {player1.current_score}\n')
                                                                            add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                                                            x = False
                                                                        else:
                                                                            print("Please try again a,b,c,d")
                                                                    except:
                                                                        print("Invalid input! Please try again!\n")

                                                                # _______________________________
                                                                
                                                            elif(user_input == 'b'):
                                                                print("\n")
                                                                print("incorrect answer b")
                                                                print("\n")
                                                                player1.current_score = current_score
                                                                player1.update()
                                                                print(f'Score: {player1.current_score}\n')
                                                                add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                                                x = False
                                                            elif(user_input == 'a'):
                                                                print("\n")
                                                                print("incorrect answer a")
                                                                print("\n")
                                                                player1.current_score = current_score
                                                                player1.update()
                                                                print(f'Score: {player1.current_score}\n')
                                                                add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                                                x = False
                                                            elif(user_input == 'c'):
                                                                print("\n")
                                                                print("incorrect answer c") 
                                                                print("\n")
                                                                player1.current_score = current_score
                                                                player1.update()
                                                                print(f'Score: {player1.current_score}\n')
                                                                add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                                                x = False
                                                            else:
                                                                print("Please try again a,b,c,d")
                                                        except:
                                                            print("Invalid input! Please try again!\n")

                                                # _______________________________
                                                
                                                elif(user_input == 'c'):
                                                    print("\n")
                                                    print("incorrect answer c")
                                                    print("\n")
                                                    player1.current_score = current_score
                                                    player1.update()
                                                    print(f'Score: {player1.current_score}\n')
                                                    add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                                    x = False
                                                elif(user_input == 'a'):
                                                    print("\n")
                                                    print("incorrect answer a")
                                                    print("\n")
                                                    player1.current_score = current_score
                                                    player1.update()
                                                    print(f'Score: {player1.current_score}\n')
                                                    add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                                    x = False
                                                elif(user_input == 'd'):
                                                    print("\n")
                                                    print("incorrect answer d") 
                                                    print("\n")
                                                    player1.current_score = current_score
                                                    player1.update()
                                                    print(f'Score: {player1.current_score}\n')
                                                    add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                                    x = False
                                                else:
                                                    print("Please try again a,b,c,d")
                                            except:
                                                print("Invalid input! Please try again!\n")

                                        # _______________________________
                                        
                                    elif(user_input == 'b'):
                                        print("\n")
                                        print("incorrect answer b")
                                        print("\n")
                                        player1.current_score = current_score
                                        player1.update()
                                        print(f'Score: {player1.current_score}\n')
                                        add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                        x = False
                                    elif(user_input == 'a'):
                                        print("\n")
                                        print("incorrect answer a")
                                        print("\n")
                                        player1.current_score = current_score
                                        player1.update()
                                        print(f'Score: {player1.current_score}\n')
                                        add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                        x = False
                                    elif(user_input == 'd'):
                                        print("\n")
                                        print("incorrect answer d") 
                                        print("\n")
                                        player1.current_score = current_score
                                        player1.update()
                                        print(f'Score: {player1.current_score}\n')
                                        add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                                        x = False
                                    else:
                                        print("Please try again a,b,c,d")
                                except:
                                    print("Invalid input! Please try again!\n")


                            # _______________________________
                            
                        elif(user_input == 'b'):
                            print("\n")
                            print("incorrect answer b")
                            print("\n")
                            player1.current_score = current_score
                            player1.update()
                            print(f'Score: {current_score}\n')
                            add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                            x = False
                        elif(user_input == 'c'):
                            print("\n")
                            print("incorrect answer c")
                            print("\n")
                            player1.current_score = current_score
                            player1.update()
                            print(f'Score: {current_score}\n')
                            add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                            x = False
                        elif(user_input == 'd'):
                            print("\n")
                            print("incorrect answer d") 
                            print("\n")
                            player1.current_score = current_score
                            player1.update()
                            print(f'Score: {current_score}\n')
                            add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                            x = False
                        else:
                            print("Please try again a,b,c,d")
                    except:
                        print("Invalid input! Please try again!\n")
# ________________________________________


            elif(user_input == 'a'):
                print("\n")
                print("incorrect answer a")
                print("\n")
                player1.current_score = current_score
                player1.update()
                print(f'Score: {current_score}\n')
                add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                x = False
            elif(user_input == 'c'):
                print("\n")
                print("incorrect answer c")
                print("\n")
                player1.current_score = current_score
                player1.update()
                print(f'Score: {current_score}\n')
                add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
                x = False
            elif(user_input == 'd'):
                print("\n")
                print("incorrect answer d") 
                print("\n")
                player1.current_score = current_score
                player1.update()
                print(f'Score: {current_score}\n')
                add_player_to_high_scores(player1.name, player1.question_level, player1.current_score)
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




def is_new_high_score():
    print('____________________________________________________')
    print(High_Scores.get_top_five())
    print('____________________________________________________')


def minimum_high_score():
    print('____________________________________________________')
    print(High_Scores.minimum_of_top_five())
    print('____________________________________________________')
    

def add_player_to_high_scores(name, highest_level, final_score):
    High_Scores.create(name, highest_level, final_score)





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



def see_all_questions():
    print('____________________________________________________')
    print(Questions.get_all())
    print('____________________________________________________')


def delete_question():
    user_input_id = input("id of question to delete: ")
    question = Questions.find_by_id(user_input_id)
    question.delete()



def delete_high_score():
    user_input_id = input("id of high score to delete: ")
    score = High_Scores.find_by_id(user_input_id)
    if(score):
        score.delete()
        print('____________________________________________________')
        print("High Score successfully deleted")
        print('____________________________________________________')
    else:
        print('____________________________________________________')
        print("\nHigh Score not found!\n")
        print('____________________________________________________')



def update_question():
    user_input_id = input("Please input the id of the question you want to update: ")
    question = Questions.find_by_id(user_input_id)
    if(question):
        user_input_what_to_update = input("Which would you like to update (level, text, correct_answer, w_answer1, w_answer2, w_answer3): ")
        if(user_input_what_to_update == "level"):
            level_input = input("Type the new level: ")
            question.level = level_input
            question.update()
            print("question has been successfully updated")
        elif(user_input_what_to_update == "text"):
            text_input = input("Type the new text: ")
            question.text = text_input
            question.update()
            print("question has been successfully updated")
        elif(user_input_what_to_update == "correct_answer"):
            correct_input = input("Type the new correct answer: ")
            question.correct_answer = correct_input
            question.update()
            print("question has been successfully updated")
        elif(user_input_what_to_update == "w_answer1"):
            wrong_input1 = input("Type the new wrong answer 1: ")
            question.w_answer1 = wrong_input1
            question.update()
            print("question has been successfully updated")
        elif(user_input_what_to_update == "w_answer2"):
            wrong_input2 = input("Type the new wrong answer 2: ")
            question.w_answer2 = wrong_input2
            question.update()
            print("question has been successfully updated")
        elif(user_input_what_to_update == "w_answer3"):
            wrong_input3 = input("Type the new wrong answer 3: ")
            question.w_answer3 = wrong_input3
            question.update()
            print("question has been successfully updated")
        else:
            print("\nThat attribute doesn't exist, please try again\n")

    else:
        print("\nThe question id you entered doesn't exist, please try again\n")
