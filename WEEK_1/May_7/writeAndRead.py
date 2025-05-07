f=open("write_and_read.txt",'w') #opening the file in write mode
st=input("Enter the contents to write to the file:") #user input for the contents of the file 
f.write(st) #writing the contents to the file
f.close() # closing the file
f=open("write_and_read.txt",'r') # opening the same file in read mode
f1=f.read() #reading the contents of the same file
print("Contents in the file:")
print(f1)
f.close()