import random
number_to_guess= random.randint(1,25)

name= input("Welcome: ")
number_of_guesses= 0

while True:
    print("Press 1 to play, 0 to exit!")
    choice= int(input("Would you like to play a game?"))
    if choice==1:
        while number_of_guesses<5:
            guess_number= int(input("Try your number: "))
            number_of_guesses+= 1
            if guess_number<number_to_guess:
                print("Low, try one more time.")
            if guess_number>number_to_guess:
                print("High, try one more time.")
            if guess_number==number_to_guess:
                print("Well played!!")
                break
            if number_of_guesses==5:
                break
    if choice==0:
        break
if guess_number==number_to_guess:
    print(f"Well, well!! Your number is {guess_number} and you made it in {number_of_guesses} steps..")
else:
    print("Maybe, you would like you to try one more time ? ")

