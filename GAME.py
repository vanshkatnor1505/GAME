
# rock , paper , scissors game 


#  1 = rock  , 2 = paper , 3 = scissors
import random


def game():
    user_score = 0
    computer_score = 0
    rounds = int(input("Enter number of rounds to play: "))

    for _ in range(rounds):
        user_choice = int(input("Enter your choice (1: Rock, 2: Paper, 3: Scissors): "))
        computer_choice = random.randint(1, 3)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 1 and computer_choice == 3) or \
             (user_choice == 2 and computer_choice == 1) or \
             (user_choice == 3 and computer_choice == 2):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

    print(f"Final Score - You: {user_score}, Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You are the overall winner!")
    elif user_score < computer_score:
        print("Sorry! The computer is the overall winner.")
    else:
        print("It's a draw!")


game()