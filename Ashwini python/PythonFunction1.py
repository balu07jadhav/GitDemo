'''xy=100
def cool():
    xy=200
    print(xy)
cool()
print(xy)'''

'''t=1 
def increment():
    global t
    t=100
    print(t)

increment()
print(t)'''

#passing arguments with default values(positional)

'''def func(i,j=100):
    print(i,j)
func(50)  #50 100
func(50,250)'''

#Keyword arguments
'''def named_args(name,greeting):
    print(greeting+" "+name)
named_args("pavan","Hi")
named_args(name='pavan',greeting='hi')
named_args(greeting='hi',name='pavan')'''

'''def my_func(a,b,c):
    print(a,b,c)
my_func(10,20,30)
my_func(10,b=20,c=30)
my_func(10,c=30,b=20)
#my_func(12,b=20,30)'''

def bigger(a,b):
    if a>b:
        return a,b
    else:
        return b,a
s=bigger(100,200)
print(s)
print(type(s))
