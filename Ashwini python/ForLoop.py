# prime number divide by 1 and itself, eg 19
num = 1
count = 0
if num>1:
    for i in range(1,num+5):
        if (num%i)==0:
            count=count+1
    if count == 2:
        print("prime")
    else:
        print("no prime")
else:
    print("Natural number")

