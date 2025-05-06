# defining the function
def login(username, password): #login function takes two parameters username and password
    # predefining the username and password
    input_username=input("Enter username:") #taking username from user
    input_password=input("Enter password:") #taking password from user
    try:
        if username==input_username and password==input_password: #checking if the given username and password are correct
            print("Login successful!") #if correct, print login successful
        else:
            raise ValueError("Invalid username or password") #if not, raise an error
    except ValueError as e: #catching the error
        print(e)


#defining the register function
def register(username, password): #register function taking two parameters username and password to create a user
    print("Registration successful!")
    return username, password #returning the username and password



#taking input from user
print("Welcome to the registration page!")
username=input("Enter username: ") 
password=input("Enter password: ") 


#calling the function
registered_username, registered_password = register(username, password) #calling the register function and storing the returned values in variables


#calling the login function
print("Welcome to the login page!")
login(registered_username, registered_password) #calling the login function with the registered username and password