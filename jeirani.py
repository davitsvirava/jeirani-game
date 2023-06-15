options = ["scissors", "stone", "paper"]

user_score = 0
computer_score = 0


for i in range(5):
    
    computer_choice = random.choice(options)
    
   
    user_choice = input("Enter your choice (scissors, stone, or paper): ")
