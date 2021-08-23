from django.shortcuts import render
from .models import  Names, LoginCreds # from models, import the classes Names and Login Creds
from faker import Faker
from pymongo import MongoClient
import socket



# Create your views here.


def index(request):
    socket.getaddrinfo('localhost', 8000) # resolve getaddrinfo failure error 
    test = ten_names()
    return render(request, 'index.html', {'persons': test})

def ten_names():
    login = LoginCreds()
    my_db, my_col = login.connections()

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

