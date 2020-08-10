dict = {"tom":12,"mor":35,"ido":120,"moshe":500,"tzipi":240}
sumFirstLast = dict["tom"]+ dict["tzipi"]
print("sum of money for tom nad tzipi: "+str(sumFirstLast))

dict.update({"idan":sumFirstLast})
print("Number of entries in dictionary: "+str(len(dict)))
print("idan" in dict.keys())
