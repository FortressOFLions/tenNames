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
        self.col = 'collection_name'
        
    def connections(self):
        client = MongoClient(f'mongodb+srv://{self.usr}:{self.passwd}@cluster0.bkmts.mongodb.net/{self.db}?retryWrites=true&w=majority') # REPLACE THIS WITH YOUR OWN CONNECTION STRING, CAN COPY PASTE DIRECTLY FROM MONGODB ATLAS
        my_db = client[self.db]
        my_col = my_db[self.col]
        return my_db, my_col
