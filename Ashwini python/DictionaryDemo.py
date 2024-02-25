friends={'tom' : '111-222-333',
         'jerry' : '666-33-111'}
print(friends)  #{'tom': '111-222-333', 'jerry': '666-33-111'}

#Retriving elements from the dictionary
print(friends['tom'])  #111-222-333

#Adding elements into  the dectionary
friends ['bob']='888-999-666'
print(friends)  #{'tom': '111-222-333', 'jerry': '666-33-111', 'bob': '888-999-666'}

#Modify elements  into the dectionary
friends['bob']=('888-999-777')
print(friends)    #{'tom': '111-222-333', 'jerry': '666-33-111', 'bob': '888-999-777'}

# delete elements the dectionary
del friends['bob']
print(friends)
