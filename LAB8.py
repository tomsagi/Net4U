from random import randint
from time import sleep
#checking if a list is fibonachi sequence or not
def CheckFiboSequence(fibo):
    for i in range(len(fibo)-2):
      if ((fibo[i]+fibo[i+1])!=fibo[i+2]):
        print("\nThis isn't fibonachi sequence")
        break
      if(i == (len(fibo)-3) and fibo[i]+fibo[i+1]==fibo[i+2]):
        print("\nThis is a fibo sequence")
        break


menu = '''1.print 100 numbers 
2.check fibonachi sequence
3.randint numbers until we get 12 or we exceed 10 tries 
'''
continuee= "yes"
while(continuee == "yes"):
    print(menu)
    menuinput= input("enter your decision: ")
    if(menuinput == "1"):
        for i in range(101):
            sleep(1)
            print(str(i))
    if(menuinput == "2"):
        fibo = []
        fibo = [int(item) for item in input("Enter the list items : ").split(',')]
        sleep(3)
        CheckFiboSequence(fibo)
    if(menuinput == "3"):
        for i in range(10):
            num = randint(0,12)
            print(str(i+1)+".drawn number: "+str(num))
            sleep(2)
            if(num==12):
                print("you drew lucky number 12!")
                break
            if(i==9 and num!=12):
                print("ten draws and 12 wasn't one of the numbers...")
    continuee = input("\nwould you like to continue? yes/no\n")


