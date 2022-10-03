# Exercise2
To Run and install

```
git clone link
```
To install all packages
```
pip install -r requirements,txt
```
To run and migrate
```
python manage.py runserver
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
## For User and Books CRUD operations
<br>http://127.0.0.1:8000/books/
<br>http://127.0.0.1:8000/users/

## For Login to jwt token, User is already created
<br>http://127.0.0.1:8000/user/login/

data =  {"email": "tomhardy@email.com",
    "password": "tom@12345"}
    
## For test test_data.py using pytest and request, make sure app is running and open new terminal with root dir and activate virtualenv
```
pytest
```
