'''t1=()
t2=(11,25,46)
t3=([1,2,3,4,5,6,8])
t4=tuple("abc")

print(t1)
print(t2)
print(t3)
print(t4)'''

'''t1=(1,15,60,100,20)
print(min(t1))  #1
print(max(t1))  #100
print(sum(t1))   #196
print(len(t1))  #5'''

'''t1=(1,15,60,100,20)
for i in t1:
    print(i,end=" ")   #1 15 60 100 20  '''

#slicing Tuple
t1=(1,15,60,100,20)
print(t1[0:4])    #(1, 15, 60, 100)
print(t1[:3])    #(1, 15, 60)
print(t1[2:])    #(60, 100, 20)

print(100 in t1)  #True
print(200 in t1)   #False

print(100 not in t1)  #False
print(200 not in t1)   #True

