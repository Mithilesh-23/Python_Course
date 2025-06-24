str1="Welcome to Mythya"
str2="World"
final_String = str1 +" " + str2
print(final_String)

nm="Mithilesh"
password ="mithil123"
pincode = '442203'
txt = "Winner never quite a game"
slogan = "A small idea make you a Successful person"
lst = '123,456,male,female,java,python,cpp,mysql'

print(nm)
print("The Goo`d says " + txt )

print(type(pincode))
# Length of string
print("Number of character in txt is " ,len(txt))

# Maximum char / largest char
print('Largest character is : ' , max(txt))

# Minimum char / Smallest Char {smallest char is always space because it has smallest ASCII value}
print('Smallest Character is : ' , min(txt))

# Count {print how many time the given string is present}
print("char is repeate :",slogan.count('a')," times")
print("String is repeate : " , slogan.count("the") , "times")

# Some function related to string style
print(slogan.upper())
print(slogan.lower())
print(slogan.capitalize())
print(slogan.title())
print(txt.swapcase())

print(slogan)

# Check whether string is in upper case or lower case
print(txt.isupper())
print(txt.islower())

# Check whther it is numeric or alphanumeric
print(pincode.isnumeric())
print(txt.isalpha())
print(nm.isalpha())
print(password.isalnum())

# Check the strting an Ending String 
print(txt.endswith("love"))
print(slogan.startswith(""))

# String Split 
print(txt.split())
print(type(lst))
print(lst.split())
print(lst.split(","))
print(lst.split(",")[2])

# if we want to give some symbol like{!, #, . , ......} we print using 
print(nm)
print(nm.center(30,'.'))  # In this mithilesh is display on center and at the left and right side dot is print 
print(nm.ljust(25,'@'))
print(nm.rjust(25,'#'))

# format
msg = "hii {} welcome to mythya world"
print(msg.format('mithil'))
print(msg.format("Charu"))

# Selcting each vvalue from list 
lst1 = ['virat','dhoni','rohit','bhuvi','pandya']
msg1 = 'hii {} welcome to my world'

for nam in lst1:
    print(msg1.format(nam))

# In this we use formate map
msg2='Hii welcome {name} to city {city}'
print(msg2.format_map({'name':'mithil','city':'Amt'}))
print(msg2.format_map({'city':'ngp','name':'mithya'}))

lst3 = ['123,456,male,female,java,python,cpp,mysql']
sss='|'
print(sss.join(['123,456,male,female,java,python,cpp,mysql']))


# strip

txt1 = '             Mithil          '
print(txt1)
print(txt1.strip())
print(txt1.lstrip())
print(txt1.rstrip())

# use for privacy as it transform the charcter eith other char 
table = str.maketrans('abcdefgs','123#$%^4')
str3="lets makes things better"
print(str3.translate(table))

slogan='Technology is power technology is the future'
print(slogan[9])
print(slogan[2:23])
print(slogan[9:])
print(slogan[:23])
print(slogan[-1])
print(slogan[::-1])   # for reverse the string

str4="jahufhciuhgoiueuxhgmiuh"
print(sorted(str4))


# checking anagram
st1='silent'
st2='listen'

if sorted(st1) == sorted(st2):
    print('anagrams')



