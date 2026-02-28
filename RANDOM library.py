import random
attempt=5
r= random.randint(1,10)
for i in range(attempt):
    try:
        guess =int(input(f"Attempt {i+1}/{attempt}-Enter your guess:"))

        if guess>r:
            print("Guess is greter")
        elif guess<r:
            print("Guess is smaller")
        else:
            print(f"you have use correct guess,you won this game", r)
            break
    except ValueError:
        print("you have entered incorrect value")
    
        if guess != attempt:
            print(f"you lose ,The correct guess is", r)

    
    
    

    
    