# 0 1 1 2 3 5 8 13 21
n1 = 0
n2 = 1
num = 10
#sum = 0
print(n1)
print(n2)
for i in range(2,num):
    sum=n1+n2
    n1=n2
    n2=sum
    print(sum)


