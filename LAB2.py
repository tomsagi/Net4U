tomato = 3
cucumber = 2
cola = 5
chicken = 20

print("prices: \nTomato - 3 NIS for kilo\nCucumber - 2 NIS for kilo\nCola - 5 NIS for a can\nChicken - 20 NIS for kilo\n")

userTomato = int(input("How many kilos of tomato would you like? "))
userCucumber = int(input("How many kilos of cucumber would you like? "))
userCola = int(input("how many cans of cola would you like? "))
userChicken = int(input("How many kilos of chicken would you like? "))

print("\nSummary of order:\nKilos of tomato: "+str(userTomato)+"\nKilos of cucumber: "+str(userCucumber)+"\nCans of cola: "+str(userCola)+"\nKilos of chicken: "+str(userChicken))

sumTomato = tomato * userTomato
sumCucumber = cucumber * userCucumber
sumCola = cola * userCola
sumChicken = chicken * userChicken
sumPrices = sumCola + sumTomato + sumChicken + sumCucumber

print("\nPrice before tax - "+str(sumPrices)+" NIS\nPrice after tax - "+str("%0.2f" %(sumPrices*1.17))+" NIS")





