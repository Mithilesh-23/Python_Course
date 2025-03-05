cho=None
c=[]

while cho != 'no':
    nm=input('Enter country name:')
    c.append(nm)
    cho=input('Do you want add more country? (yes/No) : ')


con=input('Enter a country  for search :')
if con in c:
    print('Country found')
else :
    print('Not Found')
    cho==input('Do you to add country in list (yes/no) : ')
    if cho.lower() == 'yes':
        c.append(con)
        print(c)

# Finding common values in 2 lists
lst1=[1,2,3,4,5,6,7]
lst2=[1,4,6,3,7,9]

common = [x for x in lst1 if x in lst2]
print('common values is : ' , common)

mithil = ['kava','java','js','cpp','kotlin']
charu = ['html','css','jva','js']
com=[i for i in mithil if i in charu]
print('common valuse is : ' , com)

#  to ckeck the odd and even number in list
n=[1,2,3,4,5,6,7,8,9,10]
odd=[x for x in n if x%2==1]
print('Odd values are : ' , odd)

even=[x for x in n if x%2==0]
print('Even valus are : ' , even )

# for loop with list 
lst1=[4,65,-3,2,55,-67,9,7,5,-788,4]
positive=[x for x in lst1 if x>0]
print('positive no are :' , positive)

# unique values one value appers one time only
lst=[1,3,4,5,6,7,8,9,3,4,8,1,1,2,3,456,7]
unique=[]

[unique.append(item) for item in lst if item not in unique]
print('Unique values are : ', unique)

sq=[x**2 for x in lst]
print('Square of values are : ' , sq)
