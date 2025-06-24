lst=[]
print(type(lst))

# Inserting a element in list
# Append is used to add element at the end of the list
lst.append('java')
print(lst)
lst.append('cpp')
lst.append('python')
lst.append('mysql')
print(lst)

# insert is used to add the element at specific position 
lst.insert(1,'mithil')
print(lst)

lst.insert(3,'vision')
print(lst)


# remove is used to remove the element from the list
# as it remove the first occurance of the element, 
# the element which we want to remove are written in the bracket
lst.remove('vision')
print(lst)

# Some Function related to list
print('Total element in list : ',len(lst))
print('Largest element in list :',max(lst))
print('Smallest element in list :',min(lst))

# Sort function
lst.sort()
print(lst)

# reverse function
lst.reverse()
print(lst)
