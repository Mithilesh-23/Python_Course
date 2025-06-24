# eg 1
print('Mithilesh Dhandale')
for i in range(1,11):
    print(f'Thanks {i}')

n=int(input('Enter a Number : '))
for i in range(1,11):
    print(n*i)

for num in range(51,61):
    print(num)

nm='Mithilesh'
for i in nm:
    print(i)

s = ['Mithilesh','dineshji','dhandale']
for i in s :
    print(i)

# range() function are commonly use with for loops in python to generate a sequence of number 
# It aslo be take a 1,2,3 arguments

# range(stop): Generates numbers from 0 to stop-1.
# range(start, stop): Generates numbers from start to stop-1.
# range(start, stop, step): Generates numbers from start to stop-1, incrementing by step.

# eg 1
for i in range(11):
    print(f'{i}times Mithilesh')

# eg 2
for i in range(1,10):
    print(f'{i}times Mithil')

# eg 3
for i in range(1,20,2):
    print(f'{i}times Mithu')


# eg 4 continue
name = 'Mithilesh'
for i in name:
    if i == 'h' or i == 'e' :
        continue
    else:
        print(i)

# eg 5 break 
for i in range(1,11):
    if i==5:
        break
    else :
        print(f'{i}') 
    i+=1
