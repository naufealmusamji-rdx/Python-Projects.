import random
attempt=0
max_attempt=5
r = random.randint(1,10)
while attempt < max_attempt:
    try:
        guess=int(input("Enter a number between 1-10: "))
        attempt+=1
        if guess > r:
            print("Guess is greter")
        elif guess < r:
            print("Guess is smaller")
        else:
            print("you have use correct guess,you won this game")
            exit()
    except ValueError:
        print("you have entered incorrect value")
if guess != max_attempt:
    print(f"you lose ,The correct guess is", r)    
