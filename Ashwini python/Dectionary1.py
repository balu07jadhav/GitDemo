'''values ={'a' : '100',
        'b' : '200',
        'c' : '300',
        'd' : '400'
        }
for k in values:
    print(k,":", values[k])

print(values)  #{'a': '100', 'b': '200', 'c': '300', 'd': '400'}
print(len(values))  #4   '''

'''d1= {"mike" :41, "bob" :35}
d2={"bob" :35, "mike" :41}
print(d1==d2)  #True
print(d1 != d2)  #False'''

friends={'tom':'111-222-333', 'bob':'888-999-666','jerry':'666-33-111'}
print(friends)   #{'tom': '111-222-333', 'bob': '888-999-666', 'jerry': '666-33-111'}

#popitem() Returns randomly select item fromdictionary and also remove

print(friends.popitem())   #('jerry', '666-33-111')
print(friends)   #{'tom': '111-222-333', 'bob': '888-999-666'}

#clear() delete everything from dictionary
print(friends.clear())  # None

friends={'tom':'111-222-333', 'bob':'888-999-666','jerry':'666-33-111'}
#keys() return keys in dictionary tuples
print(friends.keys())   #dict_keys(['tom', 'bob', 'jerry'])

#values() return values in dictionary tuples
print(friends.values())    #dict_values(['111-222-333', '888-999-666', '666-33-111'])

#get(key) return valueof key, if key is not found  it returns None,
#instead on throwing exception
print(friends.get('jerry'))   #666-33-111
print(friends.get('bob'))  #888-999-666

#pop (key) remove the item from the dictionary,
# if key is not found keyerror will be thrown
print(friends)     #{'tom': '111-222-333', 'bob': '888-999-666', 'jerry': '666-33-111'}
print(friends.pop('tom'))   #111-222-333
print(friends)   #{'bob': '888-999-666', 'jerry': '666-33-111'}


