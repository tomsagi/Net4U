num = 1234

'''
thousands - 1
hundreds -2 
dozens - 3
oneness - 4
'''

thousands = num//1000
hundreds = (num//100)%10
dozens = (num//10)%10
oneness = num%10

print("alafim: "+str(thousands)+"\nmeot: "+str(hundreds)+"\nasarot: "+str(dozens)+"\nahadot: "+str(oneness))