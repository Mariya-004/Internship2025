# defining a fuction to covert temperature in celsius to fahrenheit
def celsius_to_fahrenheit(celsius): 

    fahrenheit=(celsius * 9/5) + 32          #formula to convert celsius to fahrenheit
    return fahrenheit                        #returning the value of fahrenheit

 #defining a function to convert fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
    
    celsius=(fahrenheit - 32) * 5/9         #formula to convert fahrenheit to celsius
    return celsius                          #returning the value of celsius 


#main function

while True: #infinite loop to keep the program running until user chooses to exit

    #taking input from user
    print("enter 1 to covert celsius to fahrenheit")
    print("enter 2 to covert fahrenheit to celsius")
    choice=int(input("Enter your choice: ")) #taking input from user to choose the conversion type



    #calling the function based on user choice
    if choice==1:
        cel=float(input("Enter temperature in celsius: "))                 #taking input from user to convert celsius to fahrenheit
        print("Temperature in fahrenheit is: ",celsius_to_fahrenheit(cel)) #calling the function and printing the result
    elif choice==2:
        fah=float(input("Enter temperature in fahrenheit: "))
        print("Temperature in celsius is: ",fahrenheit_to_celsius(fah))
    else:
        print("Invalid choice")
    
    print("Do you want to continue? (y/n)") #asking user if they want to continue
    cont=input()          #taking input from user to continue or not
    if cont.lower()!='y': #if user enters anything other than y, exit the loop
        break              #exit the loop
