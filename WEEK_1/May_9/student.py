class Student:
    def __init__(self, ID, Name, Class, Contact):    #constructor to set data
        self.__id=ID
        self.__name=Name
        self.__class=Class                                      # private attributes, setting the data
        self.__contact=Contact

    def search (self, ID):    # to search for a student using the ID
        if self.__id==ID:
            print("Student found")
            print("ID:",self.__id)
            print("Name:",self.__name)
            print("Class:",self.__class)
            print("Contact:",self.__contact)
            return True
        else:
            return False
    def removeStudent(self,ID):    # to remove a student using the ID
        if self.__id==ID:
            print("Student removed")
            return True
        else:
            return False
Student={} # dictionary to store the student details
print('Welcome User')
while True:
        print("Enter 1 to add a student:")
        print("Enter 2 to search for a student")
        print("Enter 3 to remove a student")
        print("Enter 4 to exit")
        ch=input("Enter your choice:")
        if ch=='1':
            print("Enter the ID:")   #input details from the user
            id=input("ID:")
            print("Enter the name:")
            name=input("Name:")
            print("Enter the class:")
            classs=input("Class:")
            print("Enter the contact number:")
            contact=input("Contact number:")
            student=Student(id,name,classs,contact) # creating an object of the class and passing the details to the constructor
            Student[id]=student
            print("Student added successfully")
        elif ch=='2':
            print("Enter the ID:")
            id=input("ID:")
            if id in Student:
                student=Student[id]
                student.search(id)
            else:
                print("Student not found")
        elif ch=='3':
            print("Enter the ID:")
            id=input("ID:")
            if id in Student:
                student=Student[id]
                student.removeStudent(id)
                del Student[id]
                print("Student removed successfully")
            else:
                print("Student not found")
        elif ch=='4':
            print("Exiting program, Thank you!!!")
            break




