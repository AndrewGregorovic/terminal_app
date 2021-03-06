#!/usr/sbin/python

import os
import random
import sys
import time

from randomizer import randomizer, get_topic
from scoring import scoring, get_avg_time, print_current_score
from leaderboard import leaderboard, print_leaderboard, leaderboard_input

import question_dictionaries as qd


# clear screen function
def clear():
    if os.name == "nt":
        command = "cls"
    else:
        command = "clear"

    os.system(command)


# countdown function to be used before each question is displayed
def countdown():
    countdown_length = 3
    while countdown_length > 0:

        # first part of the write statement moves the cursor back to the left to write over the previous text
        sys.stdout.write("\u001b[10D" + f"00:0{countdown_length}")

        # need to flush the buffer to actually display the text or nothing will be shown until the function ends
        sys.stdout.flush()
        countdown_length -= 1
        time.sleep(1)


# quit function to end the game
def exit_quiz():
    clear()
    print("\n")
    print("{:^155}".format("Thanks for playing,"))
    welcome()
    time.sleep(5)
    clear()
    exit()


# welcome screen
def welcome():
    print("\n\n")
    print("                  CCCCCCCCCCCCC lllllll                    hhhhhhh                                                           tttt            !!!           ")
    print("               CCC::::::::::::C l:::::l                    h:::::h                                                        ttt:::t           !!:!!          ")
    print("             CC:::::::::::::::C l:::::l                    h:::::h                                                        t:::::t           !:::!          ")
    print("            C:::::CCCCCCCC::::C l:::::l                    h:::::h                                                        t:::::t           !:::!          ")
    print("           C:::::C       CCCCCC  l::::l    aaaaaaaaaaaaa    h::::h hhhhh           ooooooooooo       ooooooooooo    ttttttt:::::ttttttt     !:::!          ")
    print("          C:::::C                l::::l    a::::::::::::a   h::::hh:::::hhh      oo:::::::::::oo   oo:::::::::::oo  t:::::::::::::::::t     !:::!          ")
    print("          C:::::C                l::::l    aaaaaaaaa:::::a  h::::::::::::::hh   o:::::::::::::::o o:::::::::::::::o t:::::::::::::::::t     !:::!          ")
    print("          C:::::C                l::::l             a::::a  h:::::::hhh::::::h  o:::::ooooo:::::o o:::::ooooo:::::o tttttt:::::::tttttt     !:::!          ")
    print("          C:::::C                l::::l      aaaaaaa:::::a  h::::::h   h::::::h o::::o     o::::o o::::o     o::::o       t:::::t           !:::!          ")
    print("          C:::::C                l::::l    aa::::::::::::a  h:::::h     h:::::h o::::o     o::::o o::::o     o::::o       t:::::t           !:::!          ")
    print("          C:::::C                l::::l   a::::aaaa::::::a  h:::::h     h:::::h o::::o     o::::o o::::o     o::::o       t:::::t           !!:!!          ")
    print("           C:::::C       CCCCCC  l::::l  a::::a    a:::::a  h:::::h     h:::::h o::::o     o::::o o::::o     o::::o       t:::::t    tttttt  !!!           ")
    print("            C:::::CCCCCCCC::::C l::::::l a::::a    a:::::a  h:::::h     h:::::h o:::::ooooo:::::o o:::::ooooo:::::o       t::::::tttt:::::t                ")
    print("             CC:::::::::::::::C l::::::l a:::::aaaa::::::a  h:::::h     h:::::h o:::::::::::::::o o:::::::::::::::o       tt::::::::::::::t  !!!           ")
    print("               CCC::::::::::::C l::::::l  a::::::::::aa:::a h:::::h     h:::::h  oo:::::::::::oo   oo:::::::::::oo          tt:::::::::::tt !!:!!          ")
    print("                  CCCCCCCCCCCCC llllllll   aaaaaaaaaa  aaaa hhhhhhh     hhhhhhh    ooooooooooo       ooooooooooo              ttttttttttt    !!!           ")
    print("\n")
    print("{:^163}".format("\u001b[1mby Andrew Gregorovic\u001b[0m"))


# check if user tried to run app with any options and print notification messages if found
def options(opts):
    valid_options = ["--help", "--start", "--random", "--anon"]
    if len(opts) > 1:
        print("\n")
        for i in range(1, len(opts)):
            if opts[i] not in valid_options:
                print("{:^155}".format(f"{opts[i]} is not a valid option for this application."))
            elif opts[i] == "--start":
                print("{:^155}".format(f"App has been started with {opts[i]}: You will not be asked for a name, a random topic will be selected and you will be taken straight to"))
                print("{:^155}".format("the quiz for the remainder of this session."))
            elif opts[i] == "--random":
                print("{:^155}".format(f"App has been started with {opts[i]}: A random topic will be selected for you each time you take the quiz for the remainder of this session."))
            elif opts[i] == "--anon":
                print("{:^155}".format(f"App has been started with {opts[i]}: You will not be asked for a name for the remainder of this session."))
        print("\n")
    else:
        print("\n\n\n\n")


# ask user to press enter to continue
def continue_input():
    print("{:^155}".format("Press enter to continue"))
    if input("{:^77}".format("")) == "quit":
        exit_quiz()


# gets user name for the session
def get_name():
    while True:
        user_name = input("Please enter your name (must be 3-10 characters):\n").strip()

        if user_name == "quit":
            exit_quiz()

        # checks that user_name is a valid length and only contains letters of the alphabet
        elif len(user_name) < 3 or len(user_name) > 10:
            print("\nSorry that is not a valid name, remember it needs to be 3-10 characters long.\n")
        elif user_name.isalpha() == False:
            print("\nSorry that is not a valid name, it can't contain numbers or any special characters.\n")
        else:
            print(f"\n\nWelcome \u001b[4m{user_name}\u001b[0m!")
            break

    return user_name


# prints the topic and question number
def print_topic_and_question_number(topic, question_number, quiz_data):
    print("\n")
    print(f"\u001b[1m{topic}\u001b[0m")
    print("")
    print(f"\u001b[4mQuestion {i + 1}/{len(current_quiz[0])}\u001b[0m")
    print("\n")


# prints the question
def print_question(question_number, quiz_data, choices):
    print(f"{current_quiz[0][i]}\n")

    # iterate over choices to print each one
    for x in range(0, len(choices)):
        print(f"    {choices[x]}) {current_quiz[x + 1][i]}")

    print("\n\n")


# gets users answer
def get_user_answer(choices):
    while True:
        # sanitises user input so that it can be compared to valid inputs
        user_answer = input("Enter your answer: ").strip().lower()

        if user_answer == "quit":
            exit_quiz()

        # checks that input is one of the 4 choices
        elif user_answer in choices:
            break
        else:
            print("Sorry that is not one of the 4 choices, please try again.")

    return user_answer


# prints the question review
def print_question_review(question_number, quiz_data, choices, user_answer, time):
    print(f"{current_quiz[0][i]}\n")
    for x in range(0, len(choices)):

        # appends different text to each choice depending on if its the answer or the users input
        if current_quiz[5][i] == choices[x] and user_answer == choices[x]:
            print(f"   \u001b[1m\u001b[7m {choices[x]}) {current_quiz[x + 1][i]} \u001b[0m ", end="")
            print("- Correct/Your answer")
        elif current_quiz[5][i] == choices[x]:
            print(f"    \u001b[1m{choices[x]}) {current_quiz[x + 1][i]}\u001b[0m ", end="")
            print("- Correct answer")
        elif user_answer == choices[x] and current_quiz[5][i] != choices[x]:
            print(f"   \u001b[7m {choices[x]}) {current_quiz[x + 1][i]} \u001b[0m ", end="")
            print("- Your answer")
        else:
            print(f"    {choices[x]}) {current_quiz[x + 1][i]}", end=" ")
            print("")

    print("\n\n")

    # compares user_answer to the answer key and prints whether they answered correctly or not
    if user_answer == current_quiz[5][i]:
        print("Well done, you answered the question", end=" ")
        print("correctly", end=" ")
        print(f"in {time:.1f} seconds!")
    else:
        print("Good try, unfortunately you answered the question", end=" ")
        print("incorrectly", end=" ")
        print(f"in {time:.1f} seconds.")


def fun_fact(time, streak):
    if random.randint(1, 2) == 1:
        print("{:^155}".format(f"Fun fact: You had an average answer speed of {time:.1f} seconds for the questions that you answered correctly!"))
    else:
        print("{:^155}".format(f"Fun fact: Your highest answer streak for the quiz was {streak} correct answers in a row!"))


# get user input while on the results screen
def results_input():
    while True:
        print("{:^155}".format("To view the leaderboard enter 'l', otherwise would you like to take another quiz? (y/n): "))
        end_of_quiz_input = input("{:^77}".format("")).strip().lower()
        if end_of_quiz_input == "quit":
            exit_quiz()
        elif end_of_quiz_input != "l" and end_of_quiz_input != "y" and end_of_quiz_input != "n":
            print("")
            print("{:^155}".format("Sorry that isn't a valid option, please try again.\n"))
        else:
            break

    return end_of_quiz_input


# display readme if app started with --help option instead of running the quiz app
if "--help" in sys.argv:
    with open(sys.path[0] + "/help.md") as f:
        print(f.read())
else:
    # start the quiz app
    clear()
    welcome()
    options(sys.argv)
    continue_input()

    # clear screen and display the instructions/rules unless app is started with --start option
    if "--start" not in sys.argv:
        clear()
        print("\n\n\n")
        print("{:^163}".format("\u001b[4mClahoot!\u001b[0m"))
        print("\n")
        print("""Clahoot! is a multiple choice quiz game created as a terminal application based on the online Kahoot! game.
It has been adapted to a single player experience with a leaderboard rather than an online multiplayer game and follows a similar scoring style to Kahoot!.""")
        print("\n")
        print("{:^163}".format("\u001b[4mInstructions\u001b[0m"))
        print("\n")
        print("""- The app will randomly choose the length of the quiz (10-20 questions) and the questions that you will be asked.
- The questions will be from a pool of potential questions for the topic you select.
- To input your answer, type the letter corresponding to the choice you would like to select and press 'Enter'.
- Before each question is displayed there will be a short countdown. Once it ends, a hidden timer will start to track how quickly you answer the question.
- After each question you will be given time to review the question and answer before moving on. This screen will also display your current score and speed.
- You will be awarded points for each correct answer. You will receive additional points for faster answers and maintaining an answer streak.
- At the end of the quiz, your final score will be displayed along with how many questions you answered correctly and a fun fact about your performance.
- Your final score will be added to the leaderboard if it qualifies as one of the top 10 score for the current topic and question length.
- You will also have the option to view the current leaderboard for the topic you selected as well as options to play again or quit.""")
        print("\n")
        print("{:^163}".format("\u001b[1mYou can exit the app at any time by entering 'quit'\u001b[0m"))
        print("\n")
        continue_input()

    # clear screen and get user name unless app is started with --start or --anon
    clear()
    print("\n\n\n")
    if "--start" in sys.argv or "--anon" in sys.argv:
        user_name = "anonymous"
    else:
        user_name = get_name()

    # main application loop, allows user to take the quiz again without having to enter their name again but lets them choose a different topic
    while True:

        # only print if app was not started with --start or --random
        if "--start" not in sys.argv and "--random" not in sys.argv:
            print("\n\n")
            print("""Before starting there are 3 topics available for you to choose between,\n
        1) Capital Cities
        2) World Geography
        3) World Languages (Currently test questions)""")
            print("\n")

        # set the number of topics manually according to the print statement above then call the function to get users selection
        number_of_topics = 3
        selected_topic = get_topic(number_of_topics, sys.argv)

        # after getting topic selection, get the quiz data from randomizer() and set the topic to a variable
        if selected_topic == 1:
            current_quiz = randomizer(qd.capital_cities)
            quiz_topic = "Capital Cities"
        elif selected_topic == 2:
            current_quiz = randomizer(qd.world_geography)
            quiz_topic = "World Geography"
        elif selected_topic == 3:
            current_quiz = randomizer(qd.test_dict)
            quiz_topic = "World Languages"

        print("\n\n\n")
        if input("Press enter when you are ready to begin the quiz ") == "quit":
            exit_quiz()

        # initialise variables that will be used during the quiz
        choices = ("a", "b", "c", "d")

        # score data is kept as a list to make the code cleaner but it makes it slightly more confusing to keep track of what value is what piece of info
        # it is set up to be: [0] pts for current question
        #                     [1] total pts
        #                     [2] total correct answers
        #                     [3] total time for correct answers
        #                     [4] current answer streak
        #                     [5] highest answer streak
        #                     [6] previous answer streak
        score_data = [0, 0, 0, 0, 0, 0, 0]

        # loop through all the questions
        for i in range(0, len(current_quiz[0])):
            clear()

            # prints the current topic and question number, and a countdown to it being displayed, also starts a timer when the countdown ends
            print_topic_and_question_number(quiz_topic, i, current_quiz)
            countdown()
            clear()
            start_time = time.time()

            # after the countdown, reprints the topic and question number then prints the question
            print_topic_and_question_number(quiz_topic, i, current_quiz)
            print_question(i, current_quiz, choices)

            # gets the users answer for the current question
            user_answer = get_user_answer(choices)

            # stop the timer when user enters a valid answer and find the difference to get time taken
            end_time = time.time()
            time_taken = end_time - start_time
            clear()

            # reprints the question for review, showing what the correct answer was and what answer the user gave
            print_topic_and_question_number(quiz_topic, i, current_quiz)
            print_question_review(i, current_quiz, choices, user_answer, time_taken)

            # calls the scoring function and updates variables with the values returned
            score_data = scoring(current_quiz[5][i], user_answer, time_taken, score_data)

            # prints current score info as part of the review screen
            print_current_score(score_data)

            # print a different continue message depending on if it's the last question or not
            print("\n\n")
            if i + 1 != len(current_quiz[0]):
                if input("Press enter to continue to the next question ") == "quit":
                    exit_quiz()
            else:
                if input("Press enter to continue to your results ") == "quit":
                    exit_quiz()

        # get avg answer time for correctly answered questions
        avg_time = get_avg_time(score_data[3], score_data[2])

        # clear screen and display results
        clear()
        print("\n\n\n")
        print("{:^163}".format("\u001b[4mCongratulations on completing the quiz!\u001b[0m\n\n"))
        print("{:^171}".format(f"You answered \u001b[1m{score_data[2]}\u001b[0m out of \u001b[1m{len(current_quiz[0])}\u001b[0m questions correctly!\n"))
        print("{:^163}".format(f"Your final score is \u001b[1m{score_data[1]}\u001b[0m\n\n\n"))
        fun_fact(avg_time, score_data[5])
        print("\n\n\n")

        # calls leaderboard function to save the users score if it qualifies as a high score and save current leaderboard data to a variable if the user wants to view it
        current_leaderboard = leaderboard(quiz_topic, current_quiz, user_name, score_data[1])

        # need to get user input while on the results screen
        end_of_quiz_input = results_input()

        # first checks if user selected view leaderboard
        if end_of_quiz_input == "l":
            clear()

            # display leaderboard
            print_leaderboard(quiz_topic, current_quiz, current_leaderboard)

            # need to get user input again on the leaderboard screen
            end_of_quiz_input = leaderboard_input()

        # check user input to determine if the app stops or continues again, clear the screen if we continue
        if end_of_quiz_input == "y":
            clear()
            continue
        else:
            exit_quiz()
