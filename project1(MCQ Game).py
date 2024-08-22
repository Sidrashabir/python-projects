#This game ask multiple choice question about Sports. The game will also keep track of the score and it is going to print it at the end.

import time

#Welcome the user
print("Welcome to the Simple Quiz Game!")
time.sleep(1)

#Chances
chances = 1
print("You will have", chances, "chance to answer correctly. \nPlease put the alphabet of the answer\n")
time.sleep(2)

#Score
score = 0

#question number 1
question_1 = print("1) Table Tennis is also known as?\n(a) Snooker\n(b) Ping Pang\n(c) Air Hockey\n(d) Lawn Tennis\n\n ")
answer_1 = "b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_1, "\n\n")

time.sleep(2)

#question number 2
question_2 = print("2) Which team has won the most IPL title?\n(a) Kolkata Knight Riders\n(b) Sunrisers Hyderabad \n(c) Rajasthan Royals\n(d) Mumbai Indians\n\n ")
answer_2 = "d"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_2):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_2, "\n\n")

time.sleep(2)

#question number 3
question_3 = print("3) Which country has won the most FIFA World cup title?\n(a) Brazil\n(b) Italy\n(c) Germany\n(d) Argentina\n\n ")
answer_3 = "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_3, "\n\n")

time.sleep(2)

#question number 4
question_4 = print("4) Who is the first Indian Woman to win a WTA title?\n(a) Saina Nehwal\n(b) Sania Mirza\n(c) P.V Sindhu\n(d) Jwala Gutta\n\n ")
answer_4 = "b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_4):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_4, "\n\n")

time.sleep(2)

#question number 5
question_5 = print("5) Who is the highest run-scorer in IPL history?\n(a) Virat Kholi\n(b) MS Dhoni\n(c) Shikhar Dhawan\n(d) David Warner\n\n ")
answer_5 = "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_5):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_5, "\n\n")

time.sleep(1)

#print the score
while score >= 4:
    print("Well done! Your score was", score)
    break

while score <= 3:
    print("Better luck next time! Your score was", score)
    break
#Goodbye message
print("Thank you for playing the Simple Quiz Game!")