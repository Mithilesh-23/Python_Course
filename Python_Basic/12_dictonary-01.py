# Creating dictonary
dic = {
    'mithilesh','amravati'

}
dic1 = {
    'name':'mithilesh',
    'product':'Bottel',
    "model":"sigma2.0",
    "company":"sigma.pvt.lmt",
    "price":1234567
}

print(dic)
print(dic1)

# replacing one value with other
dic1['name']="charu"
print(dic1)

# adding new entry
dic1["mygear"]=2020
print(dic1)

dic1["seller"]="mythya"
print(dic1)

# printing only values
print(dic1["name"])
print(dic1["model"])

# multiple values in dictonary
pictures={
    "filmnm":["munja","kit","idiot"],
    "relyear":[2021,2023,2034,4509],
    "actor":["karan","amit","jay"]
}
print(pictures)

print(pictures['actor'])

print(pictures['actor'][1])
