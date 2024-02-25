file=open('test.txt') #open file
#print(file.read(4))  #Read file and read character by passing parameter
#print(file.readline())
#print(file.readline())

#Print line by line using readline method
'''line=file.readline()
print(line)
while line!="":
    print(line)
    line=file.readline()'''
#Print line by line using readline method
for line in file.readlines():
    print(line)






file.close() #Close file