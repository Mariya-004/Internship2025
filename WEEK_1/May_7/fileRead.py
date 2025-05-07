f=open('test.txt','r') #opening the file in read mode and assigning a filepointer
f1=f.read() #reading the entire file
words=f1.split() #splits the words in the file 
# we can also count the number of words using len(words)
count=0 #counter variable to count the number of words
for word in words:
    count+=1
print(count)
f.close() #closing the file

