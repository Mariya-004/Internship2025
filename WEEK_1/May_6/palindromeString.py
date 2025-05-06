#checking if a string is palindrome or not
def is_palindrome(s):
    st=s[::-1] #reversing the given string
    if s.lower()==st.lower(): # checking if the reversed string is equal to the actual string
        return True
    else:
        return False

#taking input from user
s=input("Enter a string: ")
#calling the function
if is_palindrome(s):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")