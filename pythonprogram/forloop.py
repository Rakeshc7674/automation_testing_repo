list=[1,2,3,4,5,6]
# print(len(list))
#
list2=[]
# for i in list:
#     list2.append(list[i])
# print(list2)

for i in range(len(list)-1,-1,-1):
    list2.append(list[i])
print(list2)
