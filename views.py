from django.shortcuts import render
from .models import  Names
from faker import Faker
from pymongo import MongoClient
import socket




# Create your views here.


def index(request):
    socket.getaddrinfo('localhost', 8000)
    test = ten_names()

    return render(request, 'index.html', {'persons': test})

def ten_names():
    client = MongoClient('') # REPLACE THIS WITH YOUR OWN CONNECTION STRING, CAN COPY PASTE DIRECTLY FROM MONGODB ATLAS
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

