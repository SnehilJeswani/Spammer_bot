import random
print("Welcome to Guess the number game!")
print("You have 3 game modes, Easy, Super easy, Medium, Hard and finally Super hard.\n In different game modes, you have to guess different modes, here is the list of numbers.\n Super easy = 0-25 \n Easy = 0-50 \n Medium = 0-100 \n Hard = 0-200 \n Super hard = 0-500.")
game_mode = input("Hard, Super hard, Medium, Super easy or Easy game mode: ")
game_mode = game_mode.capitalize()
if game_mode=='Super easy':
    print("You chose game mode as Super easy.")
    try:
        user_turns = int(input("How much turns will you need to give correct answer: "))
    except:
        print("Please enter valid input.")
    try:    
        main_number = random.randint(1,25)
        game_turns = 0
        loop_3 = 0
        def greater():
            print("Greater number please.")
        def smaller():
            print("Smaller number please.")
        while(user_turns>loop_3):
            loop_3 = loop_3+1
            try:
                user_number = int(input("Guess a number between 0-25: "))
            except:
                print("Please enter a valid input.")
            if user_number>main_number:
                smaller()
                game_turns = game_turns+1
                print("Total chances left:",user_turns-loop_3)
            elif user_number<main_number:
                greater()
                game_turns = game_turns+1
                print("Total chances left:",user_turns-loop_3)
            elif user_number==main_number:
                print("Correct answer!")
                print("You came with the correct answer in",game_turns,"turns.")
                print("The number is",main_number)
                game_turns = str(game_turns)
# ---------------------- Saving the score ----------------------- #
                main_file = open("C:\\Users\\user\\Desktop\\Programming\\Text\\Data_2.txt","a")
                main_file.write(game_turns.__add__("\n"))
                main_file.close()
                break
            if user_turns==loop_3:
                print("Chances over!!!!!!")
                print("The number was",main_number)
    except:
        print("An error occured! \nProgram crashed")
elif game_mode=='Easy':
    print("You chose game mode as Easy.")
    try:
        user_turns = int(input("How much turns will you need to give correct answer: "))
    except:
        print("Please enter a valid input.")
    try:
        main_number = random.randint(1,50)
        game_turns = 0
        loop_3 = 0
        def greater():
            print("Greater number please.")
        def smaller():
            print("Smaller number please.")
        while(user_turns>loop_3):
            loop_3 = loop_3+1
            user_number = int(input("Guess a number between 0-50: "))
            if user_number>main_number:
                smaller()
                game_turns = game_turns+1
                print("Total chances left:",user_turns-loop_3)
            elif user_number<main_number:
                greater()
                game_turns = game_turns+1
                print("Total chances left:",user_turns-loop_3)
            elif user_number==main_number:
                print("Correct answer!")
                print("You came with the correct answer in",game_turns,"turns.")
                print("The number is",main_number)
                game_turns = str(game_turns)
# ---------------------- Saving the score ----------------------- #
                main_file = open("C:\\Users\\user\\Desktop\\Programming\\Text\\Data_2.txt","a")
                main_file.write(game_turns.__add__("\n"))
                main_file.close()
                break
            if user_turns==loop_3:
                print("Chances over!!!!!!")
                print("The number was",main_number)
    except:
        print("An error occured! \nProgram crashed")

elif game_mode=='Medium':
    print("You chose game mode as Medium.")
    try:
        user_turns = int(input("How much turns will you need to give correct answer: "))
    except:
        print("Please enter a valid input.")
    try:
        main_number = random.randint(1,100)
        game_turns = 0
        loop_3 = 0
        def greater():
            print("Greater number please.")
        def smaller():
            print("Smaller number please.")
        while(user_turns>loop_3):
            loop_3 = loop_3+1
            user_number = int(input("Guess a number between 0-100: "))
            if user_number>main_number:
                smaller()
                game_turns = game_turns+1
                print("Total chances left:",user_turns-loop_3)
            elif user_number<main_number:
                greater()
                game_turns = game_turns+1
                print("Total chances left:",user_turns-loop_3)
            elif user_number==main_number:
                print("Correct answer!")
                print("You came with the correct answer in",game_turns,"turns.")
                print("The number is",main_number)
                game_turns = str(game_turns)
# ---------------------- Saving the score ----------------------- #
                main_file = open("C:\\Users\\user\\Desktop\\Programming\\Text\\Data_2.txt","a")
                main_file.write(game_turns.__add__("\n"))
                main_file.close()
                break
            if user_turns==loop_3:
                print("Chances over!!!!!!")
                print("The number was",main_number)
    except:
        print("An error occured! \nProgram crashed")

elif game_mode=='Hard':
    print("You chose game mode as Hard.")
    try:
        user_turns = int(input("How much turns will you need to give correct answer: "))
    except:
        print("Please enter a valid input.")
    try:
        main_number = random.randint(1,200)
        game_turns = 0
        loop_3 = 0
        def greater():
            print("Greater number please.")
        def smaller():
            print("Smaller number please.")
        while(user_turns>loop_3):
            loop_3 = loop_3+1
            user_number = int(input("Guess a number between 0-200: "))
            if user_number>main_number:
                smaller()
                game_turns = game_turns+1
                print("Total chances left:",user_turns-loop_3)
            elif user_number<main_number:
                greater()
                game_turns = game_turns+1
                print("Total chances left:",user_turns-loop_3)
            elif user_number==main_number:
                print("Correct answer!")
                print("You came with the correct answer in",game_turns,"turns.")
                print("The number is",main_number)
                game_turns = str(game_turns)
# ---------------------- Saving the score ----------------------- #
                main_file = open("C:\\Users\\user\\Desktop\\Programming\\Text\\Data_2.txt","a")
                main_file.write(game_turns.__add__("\n"))
                main_file.close()
                break
            if user_turns==loop_3:
                print("Chances over!!!!!!")
                print("The number was",main_number)
    except:
        print("An error occured! \nProgram crashed")

elif game_mode=='Super hard':
    print("You chose game mode as SUPER HARD.")
    try:
        user_turns = int(input("How much turns will you need to give correct answer: "))
    except:
        print("Please enter a valid input.")
    try:
        main_number = random.randint(1,500)
        game_turns = 0
        loop_3 = 0
        def greater():
            print("Greater number please.")
        def smaller():
            print("Smaller number please.")
        while(user_turns>loop_3):
            loop_3 = loop_3+1
            user_number = int(input("Guess a number between 0-500: "))
            if user_number>main_number:
                smaller()
                game_turns = game_turns+1
                print("Total chances left:",user_turns-loop_3)
            elif user_number<main_number:
                greater()
                game_turns = game_turns+1
                print("Total chances left:",user_turns-loop_3)
            elif user_number==main_number:
                print("Correct answer!")
                print("You came with the correct answer in",game_turns,"turns.")
                print("The number is",main_number)
                game_turns = str(game_turns)
# ---------------------- Saving the score ----------------------- #
                main_file = open("C:\\Users\\user\\Desktop\\Programming\\Text\\Data_2.txt","a")
                main_file.write(game_turns.__add__("\n"))
                main_file.close()
                break
            if user_turns==loop_3:
                print("Chances over!!!!!!")
                print("The number was",main_number)
    except:
        print("An error occured! \nProgram crashed")

else:
    print("Invalid gamemode!")