#TREASURE HUNT
print("WELCOME TO THE GAME OF CHOICES - TREASURE HUNT")
print("Enter 1 if you want to know HOW TO PLAY!\nEnter 2 if you want to START the game")
strt = int(input())
if strt == 1:
    print("HERE ARE THE RULES:\n1. You will be told to choose between options for various riddles, and you have 3 lives.\n2. Each time you choose a wrong option, you will loose a life.\n3. If you choose the right answer, you will be given the next question. And like this you can get hints and solve the TREASURE HUNT")
    strt = 2
if strt == 2:
    print("THE GAME IS STARTING>>>")
    q1 = input("RIDDLE 1: What has to be broken before you can use it?")
    if q1 == "egg"
