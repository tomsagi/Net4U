
#targil 1
print("Net4U, is the best \n\t ...in the world\n")


#targil 2
from datetime import datetime,date
print("current date and time:")
now = datetime.now()
today = date.today()
current_time = now.strftime("%H:%M:%S")
print(str(today)+" "+str(current_time)+"\n")

#targil 3

firstName = input("enter your first name: ")
lastName = input("enter your last name: ")
fullName = firstName+lastName
reverseName = ' '.join(fullName[::-1])
print(reverseName+"\n")


#targil 4
file = input("enter file's name: ")
for i in range(len(file)):
    if(file[i]== '.'):
        print(file[i+1:]+"\n")

#targil 5

n = int(input("enter a number: "))
nn = n*10+ n
nnn = n*100+ nn
print("the sum of "+str(nnn)+"+"+str(nn)+"+"+str(n)+"="+str(n+nn+nnn))



#targil 6

num = int(input("enter a number: "))
if(num%2 == 0):
    print("The number you entered is even!")
else:
    print("the number you entered is odd!")



#targil 8

num = 20
list1 = [10]
dict1 = {"x":200}
print("before deletion:\n"+str(num)+"\n"+str(list1)+"\n"+str(dict1))
num = 0
list1.pop()
dict1.pop("x")
print("after deletion:\n"+str(num)+"\n"+str(list1)+"\n"+str(dict1))



#targil 9

key = input("enter a key to add to dictionary: ")
value = input("enter a value to add to dictionary: ")
dict ={}
dict.update({key:value})
print("the new dictionary:\n"+str(dict))



#targil 10
dict = {}
string = input("enter a string: ")
for i in range(len(string)):
    dict.update({string[i]:i+1})
print("the new dictionary:\n"+str(dict))



#targil 11
word1 = input("enter first word: ")
word2 = input("enter the second word: ")
new_word1 = word1[:2]+word2[2:]
new_word2 = word2[:2]+word1[2:]
print("word 1:\n"+new_word1+"\nword 2:\n"+new_word2)



#targil 12
string = input("enter a string: ")
dict ={}
for i in range(len(string)):
    counter = 0
    for j in range(len(string)):
        if(string[i] == string[j]):
            counter+=1
    if(counter>1):
        dict.update({string[i]:counter})
print("the repetition of letters in the string:"+str(dict))


#targil 13
items = [2,3,5,6,7,8,9]
sum=0
for i in range(len(items)):
    sum+=items[i]
print("the sum of the items = "+str(sum))



#targil 14

list = ["Red","Green","White","Black","Pink","Yellow"]
list.pop(0)
list.pop(3)
list.pop(3)
print("the new list:\n"+str(list))
