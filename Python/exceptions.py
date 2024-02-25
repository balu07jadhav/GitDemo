IteminCart = 0

#1s way
#if IteminCart !=2:
 #   raise Exception("Product cart count not Matching")

#2nd way
if IteminCart != 2:
    pass
assert (IteminCart == 0)

try:
    with open("filelog.txt", 'r') as reader:
        reader.read()
except:
    print("Some how reached to block there is failure in try block")

finally:
    print("cleaning up resources")



 