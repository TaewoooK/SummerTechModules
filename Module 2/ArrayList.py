list=[]
list.append("Eddie")
print(list[0])
list.append(0)
for i in range(0, len(list)):
    print(list[i])
list.remove("Eddie")
for i in range(0, len(list)):
    print(list[i])