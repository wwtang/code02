import sys

from pymongo import Connection
from pymongo.errors import ConnectionFailure

def main():
    try:
        c = Connection(host='localhost',port=27017)
        print "Connect Successfully"
    except ConnectionFailure, e:
        sys.stderr.write("could not connect to MongoDB: %s " % e)
        sys.exit(1)
    
    
    #Get a database handle to a database nameed "mydb"
    dbh = c["mydb"]

    assert dbh.connection == c
    print "Successfully set up a database handle"

    #insert document

    user_doc = {
            "username": "janedoe",
            "firstname":"Jane",
            "surname":"Doe",
            "dateofbirth" : "datetime(1974,4,12)",
            "email" : "janedoe74@examole.com",
            "score" : 0          
            }
    dbh.users.insert(user_doc, safe=True)
    print "Successfylly inserted document: %s " % user_doc



if __name__=="__main__":
    main()
