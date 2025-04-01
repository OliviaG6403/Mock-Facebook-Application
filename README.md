# CYBE 465 PROGRAMMING ASSIGNMENT 1 OVERVIEW

1. This is a project that showcases a mock-facebook style application
2. The main idea of this project is that permissions for each different
    feature is crucial to the functionality of a secure system.

## Available features:
- Add friends
- Create lists
- Add friends to the lists
- Post pictures
- Comment on pictures
- Set permissions for posts (reading and writing to them)


## You will find:
- The formal code that is implemented which ensures security and access to a set of features the user may or may not use.
-- access.py

- Sample commands
-- myTest.txt
-- myTest2.txt

- A full audit of every command from the sample commands that were run
-- audit.txt

- A list of all friends
-- friends.txt

- Lists formed from the examples
-- bestfriends.txt
-- family.txt

- A list of the lists formed from the examples
-- lists.txt

- Pictures posted by users
-- coolpics.txt
-- myfirstpic.txt


## How to Begin:
- This code is written in Python
- In the command feature, type in the line below to run the sample codes
python3 access.py myTest.txt
or
python3 access.py myTest2.txt


## Available commands you can use in the application:
friendadd [friendname]
--(Adds a friend by the specified name.)

viewby [friendname]
--(Switches the current user to view the specified friend's profile.)

logout
--(Logs out the current user.)

listadd [listname]
--(Creates a new list with the specified name.)

friendlist [friendname] [listname]
--(Adds a friend to the specified list.)

postpicture [picturename.txt]
--(Posts a new picture with the specified name.)
-- MAKE SURE YOU INSERT ".txt" AT THE END OF YOUR PICTURE NAME

chlst [picturename] [listname]
--(Changes the list to which the specified picture belongs.)

chmod [picturename] [rw1] [rw2] [rw3]
--(Sets the permissions for the specified picture.)

chown [picturename] [friendname]
--(Changes the ownership of the specified picture to the specified friend.)

readcomments [picturename]
--(Reads comments from the specified picture.)

writecomments [picturename] [comment]
--(Writes a comment to the specified picture.)

end
--(Ends the session and saves all data to files.)
