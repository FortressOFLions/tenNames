from django.shortcuts import render
from .models import  Names, LoginCreds # from models, import the classes Names and Login Creds
from faker import Faker
from pymongo import MongoClient
import socket



# Create your views here.


def index(request):
    socket.getaddrinfo('localhost', 8000)
    test = ten_names()
    return render(request, 'index.html', {'persons': test})

def ten_names():
    login = LoginCreds() # store an instance of the object LoginCreds in the variable login
    client = MongoClient(f'mongodb+srv://{login.usr}:{login.passwd}@cluster0.bkmts.mongodb.net/{login.db}?retryWrites=true&w=majority') 
    db = client['ten_names']
    my_col = db['myc']
    
    pipeline = [
        {
            "$sample": {
                "size": 10
            }
        }
    ]
    
    test = my_col.aggregate(pipeline)
    people = []
    
    
    for name in test:
        people.append(name)
    
    return people

# Edited 8/23/21: Created a more secure storage/import method for the DB connection information

