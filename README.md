# Exercise Scheduler Rest API
The project consist of a Backend service using [Django REST framework](https://www.django-rest-framework.org) which allows user to login/signup create their
workout schedule and save it.The system provide **RESTAPI** for frontend to consume them for each task. 

## Table Of Content
- [Database Structure](#database-structure)
- [User Authentication](#user-authentication)
- [API endpoints](#api-endpoints)
    - [Login endpoint](#login-endpoint)
    - [Signup endpoint](#signup-endpoint)
    - [Exercises endpoint](#exercises-endpoint)
    - [Schedule endpoint](#schedule-endpoint)

## Database Structure
![db Image](output.png)
Image created using Graphiz 
- Main component of Database are:
  1. A User Table which stores user Info
  2. A Exercise table which store exercises and their details
  3. A schedule table that has User table as foreign key to store a customize user schedule 

## User Authentication
- User data is saved in **Django default User database** with some addition of fields. 
- User is authenticated with a JWT on login which expires in 5 minutes. 
- User can refresh token on a ```http://127.0.0.1:8000/token/refresh```  endpoint. refresh token is valid for 1 day.
- For more details about refer to [JWT authentication](https://django-rest-framework-simplejwt.readthedocs.io/)

## API Endpoints
### Login Endpoint
POST request to the ```http://127.0.0.1:8000/token/``` endpoint with username and password field in json format. This provide us an access token and a refresh token to access other endpoints. 
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMjM3NDY4MiwianRpIjoiODExNjMzMzFkMTJiNDc5MzgwMTkzZWRiMjhmYzg2NTkiLCJ1c2VyX2lkIjo1fQ.STPJYGJSjVH8ZneLDl0hx47vDNHXwS2A6B63rDq3tGA",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIyMjg4NTgyLCJqdGkiOiJiMTgzYzQyYTY4Y2Q0NzAyYTExOGZiN2EzYjEzMTQ4NiIsInVzZXJfaWQiOjV9.PQlYK1T0yjMK3E1n3fAHOAQBnT6dslX9fsFOC6LbI8o"
}
```
### Signup Endpoint
POST request to ```http://127.0.0.1:8000/signup/``` endpoint with username, password, email and Goal in json format will result in user creation in database. New user data will be returned if user is created

```
Output on successful user creation include everything except password field

{
    "id": 6,
    "email": "sample@gmail.com",
    "username": "sample",
    "goal": "random goal"
}
```
### Exercises Endpoint
GET request to ```http://127.0.0.1:8000/exercises/``` endpoint will return all the EXERCISES and their info saved in database.
```
Output
[
    {
        "id": 1,
        "name": "crunches",
        "details": "Crunches are for abs only and best one"
    },
    {
        "id": 2,
        "name": "pushups",
        "details": "pushups are for shoulder and chest"
    }
]
```
### Schedule Endpoints 
GET request to ```http://127.0.0.1:8000/schedule/``` endpoint will provide the all the schedule provided by current user. This endpoint is authenticated and require 
access token to access the data.
Access token can be provide in header ```Authorization: 'JWT <token>'```
```
Output
[
    {
        "User": 5,
        "time_rest": "10",
        "exc_time": "60",
        "exerciselist": [
            1
        ]
    },
    {
        "User": 5,          #user id 
        "time_rest": "20",
        "exc_time": "120",
        "exerciselist": [
            1               #exercise id
        ]
    }
]
```
POST request to ```http://127.0.0.1:8000/schedule/``` endpoint will create a schedule for current user. This endpoint is authenticated and require 
access token to access the data.
Access token can be provide in header ```Authorization: 'JWT <token>'```

```
Output 
{
    "User": 5,
    "time_rest": "20",
    "exc_time": "120",
    "exerciselist": [
        1,
        2
    ]
}
```
