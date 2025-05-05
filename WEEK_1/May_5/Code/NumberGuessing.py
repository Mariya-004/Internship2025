import random 

def number_guessing_game():
    print("******** Number Guessing Game ********")
    print("Guess a number")
    l=int(input("Enter the lower limt:"))
    u=int(input("Enter the upper limit:"))
    attempt=0
    while True:
        n=random.randint(l,u)
        attempt+=1
        print("Is the number ",n,"?")
        ans=input("Enter (y/n):")
        if ans=="y":
            print("The number is ",n," guessed in ",attempt," attempts")    
            break
        if ans=="n":
            print("Is the number greater than ",n,"?")
            ans=input("Enter (y/n):")
            if ans== "y":
                l=n+1
            elif ans=="n":
                u=n-1
            else:
                print("Invalid input!")
                break
        else:
            print("Invalid input!")
            break
number_guessing_game()
