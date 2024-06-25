print("The Love Calculator is calculating your score...")
name1 = input("What is your name?").upper()
name2 = input("What is their name?").upper()
name = name1+name2
tsum = 0
lsum = 0
# name
for i in name:
    if i == 'T' or i == 'R' or i == 'U' or i == 'E':
        tsum += 1
    if i == 'L' or i == 'O' or i == 'V' or i == 'E':
        lsum += 1

score = int(str(tsum) + str(lsum))
if (score <= 10) or (score >= 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score <= 50) and (score >= 40):
    print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
