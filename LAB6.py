
menu = '''
1. insert number and ** it by 3
2. insert 4 IPs to a list and print it 
3. insert 4 entries to DNS_dictionary and print it 
4. check if a string is a polindrom 
'''
print(menu)
insert_menu = input("choose you decision: ")

if (insert_menu == "1"):
    num = int(input("enter a number: "))
    print("your number times 3: "+str(num*3))
elif (insert_menu == "2"):
    ip1 = input("enter 1st IP: ")
    ip2 = input("enter 2nd IP: ")
    ip3 = input("enter 3rd IP: ")
    ip4 = input("enter 4th IP: ")
    ip_list = [ip1,ip2,ip3,ip4]
    print("your ip list: " +str(ip_list))
elif (insert_menu == "3"):
    dns_dict = dict()
    dns_dict.update({input("enter url: "):input("enter ip: ")})
    dns_dict.update({input("enter url: "):input("enter ip: ")})
    dns_dict.update({input("enter url: "):input("enter ip: ")})
    dns_dict.update({input("enter url: "):input("enter ip: ")})
    print("your dns list: \n"+str(dns_dict))
elif (insert_menu == "4"):
    word = input("enter a word: ")
    print("is your word a palindrom? "+ str(word == word[::-1]))
else:
    print("\nyou didn't choose an option from the menu!")

