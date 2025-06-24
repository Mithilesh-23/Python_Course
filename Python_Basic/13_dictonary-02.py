player ={
    "name":"Dhoni",
    "personal" :{
        "age":45,
        "team":"csk",
        "country":"india"
    },
    "professional":{
        "position":"wicketkeeper",
        "club":"super king",
        "jersey No":7
    },
    "records":{
        "trophy":3,
        "csk win":4
    }
    }

print(player)

print(player["name"])

print(player["personal"])

print(player["records"]["trophy"])

emp = {}
print(emp)
print(type(emp))

emp["name"]="mithilesh"
emp["number"]=33
emp["department"]="cse"
emp["location"]="amravati"
emp["salary"]=3464

print(emp)

print("Number of Elements  - ")
print(len(emp))

print("largest element : ")
print(max(emp))

print("smallest element : ")
print(min(emp))

print(emp.keys())
print(emp.values())

for keyss in emp.keys():
    print(keyss)

for val in emp.values():
    print(val)

for keyss, val in emp.items():
    print(keyss,val)

print(emp.items())

