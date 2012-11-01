import sys, shelve

def store_person(db):
    """
    Query user for data and store it in the shelf object
    """

    pid = raw_input("Enter Unique ID number: ")
    person = {}
    person['name'] = raw_input('Enter name: ')
    person['age'] = raw_input('Enter age: ')
    person['phone'] = raw_input('Enter phone: ')

    db[pid] = person

def lookup_person(db):
    """
    Query the user for the ID and desired field to fetch the 
    coressponding data from shelf object
    """
    pid = raw_input('Enter Id: ')
    field = raw_input('What would you like to know?(name, age, phone):')
    field = field.strip().lower()
    print field.capitalize() + ':' + db[pid][field]

def print_help():
    print "The avaiable commands are: "

    print "Store: store information about a person"
    print 'lookup : looks up a person from ID number'
    print 'Quit : Save Changes and exit'
    print "? : Print this message"

def enter_command():
    cmd = raw_input('Enter command (? for help): ')
    cmd = cmd.strip().lower()
    return cmd







def main():
    database = shelve.open("/Users/qitang/Desktop/database.dat")
    try:
        while True:
            cmd = enter_command()
            if cmd =="store":
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
            
    finally:
        database.close()

if __name__=="__main__":
    main()

