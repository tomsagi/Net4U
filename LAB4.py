tom_details = ["Tom Sagi",26,"tom.sagy@gmail.com","0547724151"]
print("my name: "+tom_details[0]+"\nmy age: "+str(tom_details[1])+"\nmy email: "+tom_details[2]+"\nmy phone num: "+tom_details[3])

ip_list = ["1.1.1.1","2.2.2.2"]
ip_list.append("3.3.3.3")
ip_list.append("4.4.4.4")
ip_list.append("5.5.5.5")
ip_list.pop(2)
print("\nNum of IPs we have in list: "+str(len(ip_list)))
print("The IPs: "+"\n"+ip_list[0]+"\n"+ip_list[1]+"\n"+ip_list[2]+"\n"+ip_list[3])


