# list some operation on list
sport=['cricket','football','hockey','basketball']
print(sport)
player=['Dhoni','Nemar','Sidhu','jordan',]
print(player)

sport.extend(player)
print(sport)

kit=['bat','ball','hockey bat','football','helmet']
print(kit)

sport.extend(kit)
print(sport)

print(sport[3])

print(sport[3:6])

print(sport[:6])

print(sport[4:])

print(sport[-1])

print(sport[::-1])

print(sport.pop())

print(sport)

sport.clear()

print(sport)

# Differnt data inside list
lst=[1,True,'python',3.14]
print(lst)

for i in lst:
    print(i , type(i))
    

team=['super king','indians','royal chalenger','titans',['dhoni','rohit','virat','gill']]
print(team[3])
print(team[4])
print(team[4][2])    

# how to append

team.append('ipl teams')
print(team)

team[4].append('NEMAR JR')
print(team)

# List in row col format
# list of 3x4 DD

lst=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
print(lst)

lst[1].append('MI')
print(lst)
lst[2].append('CSk')
print(lst)
lst[0].append('RCB')
print(lst)
