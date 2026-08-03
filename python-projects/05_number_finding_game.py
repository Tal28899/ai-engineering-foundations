import random
winning_num = random.randint(1,100)

while True:
    user_num =input("enter a num or type quit to exist :")
    if user_num.lower() == "quit":
        print("The game was quited...")
        break
    if not user_num.isdigit():
        print("enter a vlid num or type quit")
        continue
    #converting user_num to integer
    user_num = int(user_num)
    if user_num == winning_num :
        print ("Hurray! You Won....")
        break
    elif user_num > winning_num:
        print("Your num was too big.")
    else:
        print("Your num was too small.")

print("Game Over...!")
