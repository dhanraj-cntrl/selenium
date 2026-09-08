#dictionary -mutable/ordered/index-slicing/dupl is key not allwed

dict1= {}
dict1 = {"name" : "Dhanraj","age":23,"salary":23000}
print(dict1) #{'name': 'Dhanraj', 'age': 23, 'salary': 23000}
dict1["name"] = "Shamraj"
print(dict1)

dict1 = {"name" : "Dhanraj","age":23,"salary":23000, "name":"Shamya"}
print(dict1)   #{'name': 'Shamya', 'age': 23, 'salary': 23000}

dict1["incent"] = 10000
print(dict1)

print(dict1.items())
print(dict1.values())
print(dict1.keys())
print(dict1.get("age"))

set1 = {12,23,34,45,"pyhton",45,45,45,56}
print(set1)

set1.add(12)
print(set1)  #{34, 'pyhton', 23, 56, 12, 45}

set1.update([00,11,12])
print(set1)

#set1.remove(122)
print(set1)  #KeyError

set1.discard(122)
print(set1)

#set
#add
#update
#remove
#discard

s=set()
print(type(s))

#set=unordered/muatble/dynamic/duplicacy is not allowed

set1={12,23,34,45,5,6,7,7,7,78,89}
print(set1)

set1.add(90)   #add single element
print(set1)
set1.remove(23)
print(set1)
set1.update([111,222,333])
print(set1) #{34, 5, 6, 7, 12, 45, 78, 111, 333, 89, 90, 222}
set1.pop()
print(set1) #{5, 6, 7, 12, 45, 78, 111, 333, 89, 90, 222}

set1.clear()
print(set1)
set1={12,23,34,45,5,6,7,7,7,78,89}
print(set1)

set1 = {1,2,4,5}
set2 = {4,5,6,7}
print(set1 | set2)  #union
print(set1 & set2)  #intersection
print(set1 - set2)   #{1, 2}
print(set2 - set1)   #{6, 7}

#set1 ={[12,23,34]}
print(set1)   #set canot contain list as its unhashable

set1 = {(12,23,44)}
print(set1)

#unhashable - list/set/dictionary
#hashable- tuple/string/int/

se1=frozenset((12,23,44))

import requests
#get
response=requests.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
print(response.status_code)
#print(response.json())
assert response.status_code == 200
#post
url = "https://testautomationpractice.blogspot.com/2018/09/automation-form.html"

payload = {
    "name" : "Dhanraj",
    "age" : 23
}
response=requests.post(url,json=payload)
assert response.status_code == 201
print(response.json())

headers = {
    "Authorization": "Bearer Token",
    "Content-Type": "application/json"
}
response=requests.post(url,headers=headers)
assert response.status_code == 201





















































