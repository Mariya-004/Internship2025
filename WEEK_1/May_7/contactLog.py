def contactLog():
    dic={}
    f=open("contacts.txt","a+")
    f.write("name contact\n")
    num=int(input("Enter the number of contacts:"))
    for i in range(num):
        key=input("Enter the name:")
        value=input("Enter the contact:")
        dic[key]=value
    for name, contact in dic.items():
        f.write(name+" : "+contact+"\n")
    f.seek(0)
    print("File contents")
    print(f.read())
contactLog()