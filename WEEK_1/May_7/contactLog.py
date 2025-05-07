def contactLog():
    dic={} # creating a dictionary
    f=open("contacts.txt","a+") #opening the file in append mode
    f.write("name contact\n")
    num=int(input("Enter the number of contacts:"))
    for i in range(num):
        key=input("Enter the name:")
        value=input("Enter the contact:")
        dic[key]=value   #storing the key value pairs in a dictionary
    for name, contact in dic.items():
        f.write(name+" : "+contact+"\n") #writing the key value pairs into the dictionary
    f.seek(0) #moving the file pointer to the start of the file to read its contents
    print("File contents")
    print(f.read()) #printing the contents of the file
contactLog()