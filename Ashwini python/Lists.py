# Creating lists

'''list1=list()  #create an empty list
print(list1)

list2=list([22,31,61])
print(list2)

List3=list(["tom","jerry","spyke"])
print(List3)

List4=list("python")
print(List4)'''

#Accessing elements in list

'''l=[1,2,3,4,5]
print(l[2])
print(l[0])'''

'''list1=[2,3,4,1,30]
print(2 in list1)  #TRUE
print(2 not in list1)  #FALSE
print(len(list1))  #5
print(min(list1))  #1
print(max(list1))  #30
print(sum(list1))  #40'''

# List Slicing
'''list=[11,33,44,66,788,1]
print(list[0:5])
print(list[:5])
print(list[0:])'''

'''list1=[11,33]
list2=[1,9]
list3=list1+list2
print(list3)

list4=[1,2,3,4,5]
list5=list4 *5
print(list5)'''

list=[1,2,3,4,5]
for i in list:
    print(i,end=" ")
