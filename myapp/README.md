# **Backend - Business API**

## **Getting Started**

### **Clone Project**
From your terminal execute the command below to clone the project into your local machine
```bash
    git clone 
```

### **Install Dependencies**

1. **Python 3.9** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/project` directory and running:

```bash
pip install -r requirements.txt
```

#### **Key Pip Dependencies**

- djangorestframework==3.13.1

- djangorestframework-simplejwt


### **Set up the Database**

For now you can use a simple dbsqlite database to serve as the database for this project. Execute the commands below to automatically create one and migrate your models to it.

```bash
python manage.py makemigrations
```
and

```bash
python manage.py migrate
```

## **Tests**

Execute the command below to run tests for all endpoints:

```bash
python manage.py test
```


## **API Reference**

- BASE URL: At present this api app can only be run locally is not hosted as a base URL. The app is hosted at the default, http://127.0.0.1:8000/.

- AUTHENTICATION: This version of the api uses djangorestframework-simplejwt to create access and refresh tokens for authentication.

### **Error Handling**

Errors returned are json objects in the format shown below.

``` json5
{

    "message": string,

}
```

The Api will return six (6) error code types when requests fail:

- 400: Bad Request,
- 401: Unauthorized,
- 200: Ok,
- 201: Created,
- 204: No Content,
- 500: Internal Server Error

### **Endpoints**

#### **POST /register/**

- **General**

    - Used for registering a new user.
    
 - **Sample request url**:
``` bash 
http://127.0.0.1:8000/register/
```

- **Sample request body**:
``` json
    {"first_name": "andrew", "last_name": "mike", "username":"maesterzak","password":"mike@@1aa"}
```

 - **Sample response**

``` json
 {
    "username":"maesterzak",
    "message":"User Created Successfully. Now perform Login to get your token"
 }
```

#### **POST /api/token/**

- **General**
  - Used to login a user
  - Returns an access token and a refresh token on successfull authentication 
- **Request body**
``` json
    {
        "username":string,
        "password": string
    }
```

- **Sample request url**
  ``` bash
    http://127.0.0.1:8000/api/token/
  ```

- **Sample response**

```json5

{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2Mzk0MDc3NCwiaWF0IjoxNjYzODU0Mzc0LCJqdGkiOiJmNDM3NGFmYTI0MTI0ZTA1OTM1MWJhNGI2MmJlMzQyYSIsInVzZXJfaWQiOjIyfQ.79VFo8MVgQktutWmWv8BOs8d85S5NWs5jbhsEfHJ5u8",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYzODYyMTc0LCJpYXQiOjE2NjM4NTQzNzQsImp0aSI6IjdjMTQ0OGZkNzg2MzQwZTBiNDk0YjNjMTY2ZjgzZGY2IiwidXNlcl9pZCI6MjJ9.cjesnPnn7cmFJjVCZLki2AmReb2jO5H4aTQ-CCMEOfQ"

} 
```

#### **GET /user**

- **General**
    - Returns the details of the user making the request.

- **Request parameters**
    - Authorizations headers i.e access token for user

- **Sample request url**
  ``` bash
    http://127.0.0.1:8000/user/
  ```

- **Sample response**

```json5
{
    "message":{"username":"maesterzak",             "email":"jamew@gmail.com","first_name":"andrew","last_name":"peter"}
}
```


#### **PATCH /user**

- **General**
    - Used to update user information

- **Request body**
``` json
{
  "first_name": "andrew",
}
  ```

- **Sample request url**
  ``` bash
    http://127.0.0.1:8000/user/
  ```

- **Sample response**

```json5
{"message":"Updated successfully"}
```


#### **POST /orders**

- **General**
    -  Create new orders

- **Request body**
``` json
    {
        'user': 1,
        'transaction_id': 'randomrandoom@@',
        'total': 2000
    }
```
    
- **Sample request url**
  ``` bash
  http://127.0.0.1:8000/orders/
    
  ```

- **Sample response**

``` json
   {"order":{"id":3,"transaction_id":"ehee","total":200,"date_time":"2022-09-22T14:28:01.824710Z","user":3},"message":"Order Created Successfully."}
```

#### **GET /orders/**

- **General**
    - Gets all the orders for authenticated user making the request

- **Request parameters**
    - Authorization headers with access token

- **Sample request url**
  ``` bash
    http://127.0.0.1:8000/orders/
  ```

- **Sample response**

``` json
 {"message":"success","data":[{"id":4,"transaction_id":"hbarhbarhbar","total":100,"date_time":"2022-09-22T15:08:02.138772Z","user":22}]}
```



## Deployment N/A

## Authors
Abubakar Zakari

