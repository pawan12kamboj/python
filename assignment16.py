#question number one
import pymongo
client=pymongo.MongoClient()
database=client['students']
collection=database['student']

#question number two and three
x=0
while(x<10):
    try:
        name = input("ENTER NAME: ")
        marks = int(input('ENTER MARKS: '))
        if(marks<0 or marks >100):
            raise ValueError('Invalid marks')
            x=x-1
        else:
            collection.insert_one({'Name':name,'Marks':marks})
            x=x+1
    except  ValueError as msg:
        print(msg)

#question number four
info=collection.find({"Marks":{"$gt":80}})
for i in info:
    print(i)