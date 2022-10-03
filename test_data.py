import pytest
import requests

usrurl= "http://127.0.0.1:8000/"

def test_create_user():
    data={
    "email": "tom@curse.com",
    "username": "Tom-Curse",
    "password": "tom@curse",
    "role": "SELLER"
    }
    addurl = "users/"
    result=requests.post(usrurl+addurl,json=data)
    assert result.status_code == 201

def test_login_user():
    data={
    "email": "tom@hardy1.com",
    "password": "tom@hardy",
    }
    addurl = "user/login/"
    result=requests.post(usrurl+addurl,json=data)
    assert result.status_code == 200
def test_book():
    data = {
    "title": "Python Programming",
    "genre": "EDUCTION",
    "review": 3,
    "favorite": False
    }
    addurl = "books/"
    result=requests.post(usrurl+addurl,json=data)
    assert result.status_code == 201