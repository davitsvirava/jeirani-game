import random


options = ["scissors", "stone", "paper"]

user_score = 0
computer_score = 0


for i in range(5):
    
    computer_choice = random.choice(options)
    
   
    user_choice = input("Enter your choice (scissors, stone, or paper): ")
    
    
    if user_choice == computer_choice:
        print("Tie!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        user_score += 1
    elif user_choice == "paper" and computer_choice == "stone":
        print("You win!")
        user_score += 1
    elif user_choice == "stone" and computer_choice == "scissors":
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1


print("Final scores:")
print(f"You: {user_score}")
print(f"Computer: {computer_score}")
