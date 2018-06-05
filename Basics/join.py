mylist = ['a','b','c','d']

newString = ''

#for c in mylist:
#    newString+= c + ','
#
#print(newString)

#efficient manner
newString=",".join(mylist)
print(newString)

#join takes as a parameter a sequence type
# for example it can be used with strings

liststring = "adsflskjfalsjf;sadf"
print(','.join(liststring))

# more tricks with join

numbers="123456789"

string="Missisipi ".join(numbers)
print(string)