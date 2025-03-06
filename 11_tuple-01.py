t=(1,2,3,4,5)
print(t)
print(type(t))

print(t[0],t[3])

t1=(1,3,5,7,9,2,4,7,2,2,3,4,5)
print(t1)

t[1]=89         # this is not possible in tuple
print(t1)

print(t1)
print(*t1)
list(map(lambda x: print(x,end=" ") , t1))

t2=(1,2,3,4,5,6,7,8,7,6,5,4,3,23,2)
for x in t2:
    print(x , end=" ")

tup1=(1,2,3,4,5)
tup2=(6,7,8,9,0)

print(tup1 + tup2)

print(tup1[:3])
print(tup2[3:])
print(tup1[::-1])

print(len(tup2))

tup3=('mith',123,'charu',456,True)
print(tup3)
print(type(tup3))

tup4=['mith',675,'mithil',False]
lst = tuple(tup4)
print(lst)
print(type(lst))
