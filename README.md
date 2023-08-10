AirBnB Clone
This is a command line interpreter that mimics some basic functionality of the AirBnB website.

Description
The AirBnB clone interpreter allows users to manage objects like Users, Places, Amenities etc. Users can create, update, and destroy objects as well as view lists of objects and individual object details.

Usage
To start the interpreter:

$ ./console.py

From the interpreter prompt, you can use commands like:

create <class-name> - Creates a new instance of the class
show <class-name> <id> - Shows details of an object
all <class-name> - Prints all instances of a class
destroy <class-name> <id> - Destroys an object
update <class-name> <id> <attribute> <value> - Updates attribute of an object


EXAMPLES:


$ ./console.py
(hbnb) create BaseModel
119be8d4-6788-4535-88c6-484eebff1130
(hbnb) all BaseModel
["[BaseModel] (119be8d4-6788-4535-88c6-484eebff1130) {'id': '119be8d4-6788-4535-88c6-484eebff1130', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}"]
(hbnb) show BaseModel 119be8d4-6788-4535-88c6-484eebff1130 
[BaseModel] (119be8d4-6788-4535-88c6-484eebff1130) {'id': '119be8d4-6788-4535-88c6-484eebff1130', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb) destroy BaseModel 119be8d4-6788-4535-88c6-484eebff1130
(hbnb) show BaseModel 119be8d4-6788-4535-88c6-484eebff1130
** no instance found **


AUTHORS
Zaki-prod - Email: zakiprod04@gmail.com
Henok-Haile -Email: henokhaile53@gmail.com
