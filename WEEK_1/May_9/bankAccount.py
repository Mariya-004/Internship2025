class Bank:

    # constructor to create an account and set the details
    def __init__(self, Name, Age, AccNo, Pin):

        self.__name=Name
        self.__age=Age                      # private variables(attributes)
        self.__accNo=AccNo
        self.__pin=Pin
        self.__bal=0                     # setting the initial balance to zero during account creation
        print("Account created successfully")

    def validateCredentials(self, AccNo, pin):    # to validate if the user has entered the correct account number and password

        if AccNo==self.__accNo and pin==self.__pin:
            print("Welcome user")
            print("Name:",self.__name)
            print("Account Number:",self.__accNo)
            return True
        else: 
            return False

    def userDetails(self):
 
        print("Account Number:",self.__accNo)   # to print the user details
        print("Name:",self.__name)
        print("Age:",self.__age)
    
    def depositMoney(self, money):

        self.__bal+=money     # updating the balance according to the deposit happening
        print("Deposit succesful")

    def withdrawMoney(self, money):
        if self.__bal>=0 and self.__bal>=money:
             self.__bal-=money
             print("Withdrawal successful")    # updating the balance according to the withdraw happening
        else:
            print("Insufficient balance")
    
    def getBalance(self):

        return self.__bal

accounts = {}
print('Welcome User')
while True:
        print("Enter 1 to create an account:")
        print("Enter 2 to deposit money")
        print("Enter 3 to withdraw money")
        print("Enter 4 to get balance")
        print("Enter 5 to exit")
        ch=input("Enter your choice:")
        if ch=='1':
            print("Enter your Name:")   #input details from the user
            name=input("Name:")
            print("Enter your age:")
            age=input("Age:")
            print("Enter the account number:")
            accNo=input("Account number:")
            print("Enter the pin:")
            pin=input("Pin:")
            if accNo in accounts: # checks if the account has been already created
                print("account already exists")
            else:
                accounts[accNo]=Bank(name,age,accNo,pin) #setting the details using the constructor
                accounts[accNo].userDetails()
            print()

        # choices for user operations

        if ch == '2':
            acc=input("Enter the account number:")
            if acc in accounts:
                pin=input("Enter the pin:")
                accounts[acc].validateCredentials(acc, pin)
                amt=int(input("Enter the amount:"))
                accounts[acc].depositMoney(amt)
            else:
                print("Invalid credentials")
            print()
        if ch=='3':
            acc=input("Enter the account number:")
            if acc in accounts:
                pin=input("Enter the pin:")
                accounts[acc].validateCredentials(acc, pin)
                amt=int(input("Enter the amount:"))
                accounts[acc].withdrawMoney(amt)
            else:
                print("Invalid credentials")
            print()
            
        if ch=='4':
            acc=input("Enter the account number:")
            if acc in accounts:
                pin=input("Enter the pin:")
                accounts[acc].validateCredentials(acc, pin)
                print("The remaining balance in your account is:",accounts[acc].getBalance())
            else:
                print("Invalid credentials")
            print()
        if ch=='5':
            print("Exiting the program thank you!!!")
            break





    




    