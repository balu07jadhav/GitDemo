'''for x in range(10):
    print(x)  # 1 2 3 4..9

list1=[x for x in range(10)]
print(list1)    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list1=[x+1 for x in range(10)]
print(list1)    #[1, 2, 3, 4, 5, 6, 7, 8, 9,10]

for x in range(10):
    if(x %2 ==0):
        print(x)  #0 2 4 6 8'''

for x in range(10):
    if(x %2 ==0):
        print(x)

list1=[x for x in range(10) if x %2 ==0]
print(list1)
