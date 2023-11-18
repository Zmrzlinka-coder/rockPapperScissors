#Tuples

mytuple= tuple(('Dave',42, True))
anotherTuple=(1,4,2,8,2,2)

print(mytuple)
print (type(mytuple))
print (type(anotherTuple))

newlist= list(mytuple)
newlist.append('Neil')
newtuple=tuple(newlist)
print(newtuple)

(one,*two,hey)=anotherTuple
print(one)
print(two)
print(hey)

print(anotherTuple.count(2))