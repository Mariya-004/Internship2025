import random

def number_guessing_game():
    print("******** Number Guessing Game ********")
    print("Guess a random integer")
    l=int(input("Enter the lower limit:"))
    u=int(input("Enter the upper limit:"))
    attempts = 0
    while True:
        random_number = random.randint(l, u)
        attempts += 1
        print("Is it ", random_number, "?")
        response=(input("y/n:"))
        if response=="y":
            print("The number is ", random_number)
            print("Number guessed in ", attempts, " attempts")
            break
        elif response=="n":
            mid=(int((l+u)/2))
            print("Is it less than ", mid, "? (y/n):")
            a=input()
            if a=="y" or "Y":
                u=mid
                l=l
                random_number = random.randint(l, u)
            elif a=="n" or "N":
                l=mid
                u=u
                random_number = random.randint(l, u)
            else:
                print("Invalid input!")
                break
        else:
            print("Invalid input!")
            break       
number_guessing_game()
            