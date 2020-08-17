
#Targil 1

print("Twinkle,twinkle,little star,\n\tHow i wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinlke,twinkle,little star,\n\tHow i wonder what you are")


#Targil 2

color_list = ["Red","Green","White","Black"]
print(color_list[0]+" "+color_list[3])



#Targil 3

n = int(input("enter a number: "))
nn = n*10+ n
nnn = n*100+ nn
print("the sum of "+str(nnn)+"+"+str(nn)+"+"+str(n)+"="+str(n+nn+nnn))


#Targil 4

from datetime import date
begin = date(2014,7,2)
last = date(2014,7,21)
days = last - begin
print(days.days)


#Targil 5

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))
if(num1 == num2 and num1 == num3):
    print("three times the sum is: "+str(num1*3))
else:
    print("the average of the numbers is: "+str((num1+num2+num3)/3))



#Targil 6

num1 = int(input("enter first number: "))
num2 = int(input("enter the second number: "))
if(num1+num2>=15 and num1+num2<=20):
    print("20")
else:
    print("the sum of the two number: "+str(num1+num2))


#Targil 7

name = input("enter your name: ")
age = input("enter your age: ")
address = input("enter your address: ")
print("\nyour name: "+name+"\nyour age: "+age+"\nyour address: "+address)




#Targil 8

num1 = int(input("enter first num: "))
num2 = int(input("enter second num: "))
print("the result of (x+y)^2 is: "+str((num1*num2)**2))



#Targil 9


feet = int(input("Feet: "))
inches = int(input("Inches: "))
inches += feet * 12
cm = round(inches * 2.54, 1)
print("Your height is : %d cm." % cm)


#Targil 10

num = int(input("enter a number: "))
sum = 0
for i in range(num):
    sum+= (i**3)
print(str(sum))