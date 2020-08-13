from random import randint
from time import sleep

print("welcome to the cube game!\n")
money = int(input("enter amount of money to start with: \n"))
stop = "c"
print("amount of money entered: "+str(money)+"\n")
print("each game costs 3 NIS, good luck!\n")
sleep(3)
while(stop!="q" or money<3):
        money-=3
        print("Left amount of money: "+str(money))
        print("Drawing two numbers...")
        sleep(4)
        num = randint(1,7)
        print("first drawn number is: "+str(num))
        sleep(4)
        num2 = randint(1,7)
        print("second drawn number is: "+str(num2))
        sleep(4)
        if(num ==num2 and num ==6):
            print("you won 1000 NIS!")
            money+=1000
            print("current amount of money: " + str(money)+"\n")
        elif(num==num2):
            print("you won 100 NIS!")
            money+=100
            print("current amount of money: " + str(money)+"\n")
        elif(num!=num2 and num2==2):
            print("you won 40 NIS!")
            money += 40
            print("current amount of money: " + str(money)+"\n")
        elif(num!=num2 and num==1):
            print("you won 20 NIS!")
            money += 20
            print("current amount of money: " + str(money)+"\n")
        else:
            print("No reward this time. better luck next time!\n")
        sleep(3)
        stop = input("would you like to continue? press 'c' to continue or 'q' to quit\n")
print("your amount of money after quiting: "+str(money)+"\n")
