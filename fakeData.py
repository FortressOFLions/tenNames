from faker import Faker
from pymongo import MongoClient
import csv
from blogrpdit.models import LoginCreds



from faker import Faker
from pymongo import MongoClient
import csv
from blogrpdit.models import LoginCreds


# read contents of CSV into a dictionary 
def csv_read_into_dict():
    # Open Doc
    doc = open('names.csv', 'r')
    # Create reader
    reader = csv.DictReader(doc)
    # Create Loop
    data = []
    login = LoginCreds()
    my_db, my_col = login.connections()
    for f in reader:
        # append the line that was just read into the array 'data' as a dictionary
        data.append(dict(f))
        # insert the data into mongoDB
        insertion = my_col.insert_one(dict(f))
    return data

# Create a csv doc of made-up data
def create_data():
    # Instantiate Faker
    fake = Faker()
    # Open/create document 
    my_doc = open('names.csv', 'w')
    # Create header 
    header = ['name', 'street', 'city', 'zipcode']
    # create an instane of a csv.writer and store it in the printer variable
    printer = csv.writer(my_doc)
    # using the printer object's 'writerow'  funciton,  insert the headers
    printer.writerow(header)
    for r in range(1000): 
        # writerow each fake piece of data 
        printer.writerow((fake.name(),fake.street_address(), fake.city(), fake.zipcode()))
        
 
# Changelog:
# 8/23/2021 - deleted outdated function and reformatted code. Commented for my own learning's sake. implimented new mongoDB connection method 


