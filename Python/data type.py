print('Hello')
a, b, c = 4, 5, 'hi'
print("value of a", + b)
print("{} {}".format("value of c", c))
print(type(a))
print(type(b))
print(type(c)) # print data type

#list data type
values=[1, 3, 'rahul', 4, 5]
print(values[0]) #print zero index values
print(values[2]) #print second index values
print(values[-1])  #give last value
print(values[1:3]) #print middle values
values.insert(3,'shetty') #insert values in list
print(values)
values.append('end') #insert values in end in list
print(values)
values[2]='RAHUL'  #Update value in list
del values[0]  #delete values in list
print(values)

#Interger
a = 5
print("The type of a", type(a)) #Print type of data
b = 40.5
print("The type of b", type(b))
c = 1+3j
print("The type of c", type(c))
print(" c is a complex number", isinstance(1+3j,complex))

#Dictionary
d = {1:'Jimmy', 2:'Alex', 3:'John', 4:'Mike'}
print(d)
print("1st name "+d[1])
print(d.keys())
print(d.values())

#Boolean
print(type(True))
print(type(False))

#Tuple
val=(12, 15, "rahul", 20)
print(val[1])
#val[2] = 'RAHUL'

#How to create run time dictionary?
dict = {}
dict["Fistname"] = "Balu"
dict["Lastname"] = "Jadhav"
dict["Gender"] = "Male"
print(dict)
print(dict["Gender"])

#Set
set1 = {'James', 2, 3, 'Python'}
print(set1)
set1.add(10)  #adding value in set
print(set1)
set1.remove(2)
print(set1)

#string
str = "string usingdouble quotes"
print(str)
s ='''A multiline 
string'''
print(s)
#operation on string
str1 = 'hello world'
str2 = 'how are you'
print(str1[0:2]) #printing first two char
print(str1[4]) #printing 4th char in string
print(str1*2)
print(str1 + str2)
