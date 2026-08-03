word = "github"
guess_count = 0

while guess_count < 3 :
    user_word = input("enter your word  :" )
    guess_count += 1 
    if user_word.lower() == word.lower():
        print("yeahhh ! You won")
        print(f"you guessed the word at {guess_count} guess")
        break 
    elif guess_count < 3 :
        print("your word was incorrect.\nTry again")
        
    else:
        print("You lose..!")
        


print("Challange is over.")
