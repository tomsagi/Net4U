from time import sleep

def menuInsert():
    menu = '''menu:\n1.Dogs Details
2.Friends List
3.N azzeret
    '''
    print(menu)
    sleep(2)
    decision = int(input("enter your decision: "))
    return decision

def DogsDetails():
    name = input("enter your dogs name: ")
    sleep(1)
    breed = input("enter your dogs breed: ")
    sleep(1)
    age = int(input("enter your dogs age: "))
    sleep(1)
    print("\nYour dog "+name+" of breed "+breed+" is "+str(age*7)+" years old in dog years\n")
    sleep(2)

def FriendsList():
    list = []
    list = [str(item) for item in input("Enter 5 friend's names seperated by ',': ").split(',')]
    sleep(2)
    name = input("enter a name to see if is in the list: \n")
    sleep(2)
    if name in list:
        print(name+ " is in the list\n")
    else:
        print(name+ " isn't in the list\n")
    sleep(2)

def NAzzeret():
    num = int(input("enter a num: "))
    sum=1
    sleep(2)
    for i in range(1,num+1):
        sum*=i
    print("the azeret of the num is: "+str(sum)+"\n")
    sleep(2)

continuee = "yes"
while(continuee == "yes"):
    decision = menuInsert()
    if(decision == 1):
        DogsDetails()
    elif(decision == 2):
        FriendsList()
    elif(decision == 3):
        NAzzeret()
    else:
        sleep(2)
        print("Not an option from the menu! try again...\n")
        sleep(1)
        continue
    continuee = input("would you like to continue the program? yes/no \n")
    sleep(1)
print("Goodbye :)\n")