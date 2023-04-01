import random

def rps():
    rng = random.randint(1,3)
    play = input("lets play rock, paper, scissors!")
    game = {1:"rock", 2:"paper", 3:"Scissors"}

    print(play)

    if rng == 1:
        computer = game[1]
    elif rng == 2:
        computer = game[2]
    else:
        computer = game[3]


    

    if play == computer:
        print("It's a tie!")
    elif play.lower() == "rock": 
        if computer == game[2]:
            print(computer)
            print("You have lost!")   
        else:
            print(computer)
            print("rock destroys scissors!,You win")
    elif play.lower() == "paper":
        if computer == game[3]:
            print(computer)
            print("scissors cuts paper, You lose!")
        else:
            print(computer)
            print("paper covers rock, you win")  
    elif play.lower() == "scissors":
        if computer == game[1]:
            print(computer)
            print("rock destroys scissors!, You lose")
        else:
            print(computer)
            print("Scissors cuts through paper!,You win")    
    else:
        print("not rps dummy")

    

    replay = input("Would you like to play again? y/n")
    if replay == "y":
        rps()
    else:
        print("Thank you for playing")


rps()



# replay = input("Would you like to play again? y/n")
# if replay == "y":
#     rps()
# else:
#     print("Thank you for playing")















# tuple = (1,2,3)
# list1 = list(tuple)
# print(type(list1))
# #for x in tuple:
#     #x = x+1
#     #print(x)
    
# tuple1 = (1,2,3)
# tuple1 = tuple1 + (4,5,6)
# print(tuple1)



