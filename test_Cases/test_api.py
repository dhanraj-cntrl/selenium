from wsgiref import headers

from selenium import webdriver
import requests

url = "https://reqres.in/api/users/2"


def test_get_user():

    response=requests.get(url)
    assert response.status_code == 200

    data=response.json()
    assert data["id"] == 21

def test_post_user():

    payload = {
        "name":"Dhanraj",
        "email":"draj@gmail.com"
    }
    headers = {
        "Authorization" : "Bearer Token",
        "Content-Type" : "application/json",
        "Accept" : "application/json"
    }

    response=requests.post(url,headers=headers,json=payload)
    assert response.status_code == 201

def test_auth():
    payload = {
        "username":"Dhanraj",
        "password":"admin123"
    }
    headers = {
        "Content-Type" : "application/json",
    }
    respo=requests.post(url,headers=headers,json=payload)
    assert respo.status_code == 200



# st = "Dhanraj Lahu Rajmane"
#
# result=[]
# for i in st.split():
#     if i=="Lahu":
#         result.append(i)
#     else:
#         result.append(i[::-1])
# print(" ".join(result))











