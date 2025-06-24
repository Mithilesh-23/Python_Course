
account={
    "accno":123456,
    "accnm":"sharayu",
    "gender":"female",
    "age":29,
    "acctype":"fixed",
    "branch":"Andheri Mumbai",
    "balance":25900.0
    }

key=input("Enter key to search : ")

if key in account:
  print(account[key])
else:
  print('data not found')

  dic={}.fromkeys(['science','maths','english'],0)
print(dic)
