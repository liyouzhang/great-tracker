from pymongo import MongoClient
from bson.objectid import ObjectId

#get the connection
client = MongoClient('mongodb://localhost:27017')

#create the collection grades
grades = client.tracker.grades

# for _ in range(3):
#     name = input('student name:')
#     klass = input('student class:')
#     grade = float(input('grade:'))
#     #print(name,klass,grade)
#     d = {'name':name,'klass':klass,'grade':grade}
#     grades.insert_one(d)

# in grades, there documents    
total = 0
c = grades.find().count()
for g in grades.find():
    total += g['grade']

print(total/c)    