from django.db import models

# Create your models here.

class Names():
    id : str
    name : str
    address : str
    city : str
    zipcode : int 

class LoginCreds(): # Mongodb Connection information 
    
    def __init__(self): # replace the values with your own login information 
        self.usr = 'username' 
        self.passwd = 'password'
        self.db =  'database_name'
