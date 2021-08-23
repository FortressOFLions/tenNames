from faker import Faker
from pymongo import MongoClient
import csv
from models import LoginCreds


login = LoginCreds()
client = MongoClient(f'mongodb+srv://{login.usr}:{login.passwd}@cluster0.bkmts.mongodb.net/{login.db}?retryWrites=true&w=majority')
my_col = client.myc

fake = Faker()
# read contents of CSV into a dictionary 
def csv_read_into_dict():
    # Open Doc
    doc = open('names.csv', 'r')
    # Create reader
    reader = csv.DictReader(doc)
    # Create Loop
    data = []
    for f in reader:
        # append the line that was just read into the array 'data' as a dictionary
        data.append(dict(f))
        # insert the data into mongoDB
        insertion = my_col.insert_one(dict(f))
    return data

# Create a csv doc of made-up data
def create_data():
    my_doc = open('names.csv', 'w')
    header = ['name', 'street', 'city', 'zipcode']
    printer = csv.writer(my_doc)
    printer.writerow(header)
    for r in range(1000):
        printer.writerow((fake.name(),fake.street_address(), fake.city(), fake.zipcode()))


# with open('names.csv', 'w') as my_doc:
#     fake = Faker()
#     header = ['name', 'street', 'city', 'zipcode']
#     printer = csv.writer(my_doc)
#     printer.writerow(header)
#     for r in range(1000):
#         printer.writerow((fake.name(),fake.street_address(), fake.city(), fake.zipcode()))

# Original iteration of the data creation function, I kept in for my own learning sake 

