list1=[2,3,4,1,32,4]
list1.append(19)
print(list1)

print(list1.count(4))

list2=[99,54]
list1.extend(list2)
print(list1)

print(list1.index(32))

list1.insert(1,25)
print(list1)  #[2, 25, 3, 4, 1, 32, 4, 19, 99, 54]

print(list1.pop(2))  #3
print(list1)  #[2, 25, 4, 1, 32, 4, 19, 99, 54]

list1.remove(32)
print(list1)  #[2, 25, 4, 1, 4, 19, 99, 54]

list1.reverse()
print(list1)   #[54, 99, 19, 4, 1, 4, 25, 2]

list1.sort()
print(list1)   #[1, 2, 4, 4, 19, 25, 54, 99]

