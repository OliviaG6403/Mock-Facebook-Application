import sys
import json

# Current user
user = ''
# Owner user
owner = ''
# Tracks the number of lines
line_ct = 0
list_of_friends = []
list_of_names = []
list_of_pictures = []

# Files
# audit_fl = ''
audit_fl = open("audit.txt", "a")
lists_fl = ''
pictures_fl = ''

first_word = True


def commands(cmd):
    global first_word

    if cmd[0] == 'friendadd':
        if len(cmd) > 2:
            print("Invalid input, too many commands.")
            audit_fl.write("Invalid input, too many commands.\n")
        else:
            friendadd(cmd[1])
    elif cmd[0] == 'viewby':
        if len(cmd) > 2:
            print("Invalid input, too many commands.")
            audit_fl.write("Invalid input, too many commands.\n")
        else:
            viewby(cmd[1])
    elif cmd[0] == 'logout':
        if len(cmd) > 1:
            print("Invalid input, too many commands.")
            audit_fl.write("Invalid input, too many commands.\n")
        else:
            logout()
    elif cmd[0] == 'listadd':
        if len(cmd) > 2:
            print("Invalid input, too many commands.")
            audit_fl.write("Invalid input, too many commands.\n")
        else:
            listadd(cmd[1])

    elif cmd[0] == 'friendlist':
        if len(cmd) > 3:
            print("Invalid input, too many commands.")
            audit_fl.write("Invalid input, too many commands.\n")
        else:
            friendlist(cmd[1], cmd[2])

    elif cmd[0] == 'postpicture':
        if len(cmd) > 2:
            print("Invalid input, too many commands.")
            audit_fl.write("Invalid input, too many commands.\n")
        else:
            postpicture(cmd[1])

    elif cmd[0] == 'chlst':
        if len(cmd) > 3:
            print("Invalid input, too many commands.")
            audit_fl.write("Invalid input, too many commands.\n")
        else:
            chlst(cmd[1], cmd[2])

    elif cmd[0] == 'chmod':
        if len(cmd) > 5:
            print("Invalid input, too many commands.")
            audit_fl.write("Invalid input, too many commands.\n")
        else:
            chmod(cmd[1], cmd[2], cmd[3], cmd[4])

    elif cmd[0] == 'chown':
        if len(cmd) > 3:
            print("Invalid input, too many commands.")
            audit_fl.write("Invalid input, too many commands.\n")
        else:
            chown(cmd[1], cmd[2])

    elif cmd[0] == 'readcomments':
        if len(cmd) > 2:
            print("Invalid input, too many commands.")
            audit_fl.write("Invalid input, too many commands.\n")
        else:
            readcomments(cmd[1])

    elif cmd[0] == 'writecomments':
        if len(cmd) > 2:
            for i in range(2, len(cmd)):
                writecomments(cmd[1], cmd[i])
            first_word = True

    elif cmd[0] == 'end':
        if len(cmd) >= 2:
            print("Invalid input, too many commands.")
            audit_fl.write("Invalid input, too many commands.\n")
        else:
            end()

    else:
        print("Invalid Command")
        audit_fl.write("Invalid Command\n")


def friendadd(friendname):
    global user
    global owner
    global list_of_friends

    file = open('friends.txt', "a")

    if user == owner:
        if friendname in list_of_friends:
            print(friendname + " is already a friend")
            audit_fl.write(friendname + " is already a friend\n")
        else:
            if owner == '':
                owner = friendname
            print(friendname + " is now your friend! YAY")
            audit_fl.write(friendname + " is now your friend! YAY\n")
            list_of_friends.append(friendname)
            file.write(friendname)
            file.write("\n")
    else:
        print("Invalid input. You're not root")
        audit_fl.write("Invalid input. You're not root.\n")
    file.close()


def viewby(friendname):
    global user
    global list_of_friends

    if user == '':
        if friendname in list_of_friends:
            user = friendname
            print(user + " is viewing the profile")
            audit_fl.write(user + " is viewing the profile\n")
        else:
            print("Invalid input." + friendname + " doesn't exist")
            audit_fl.write("Invalid input." + friendname + " doesn't exist\n")
    else:
        print("Failed to Login... only one login at a time is allowed.")
        audit_fl.write("Failed to Login... only one login at a time is allowed.\n")


def logout():
    global user
    if user == '':
        print("Invalid input. You are already logged out.")
        audit_fl.write("Invalid input. You are already logged out.\n")
    else:
        print("Goodbye " + user + ", you've successfully logged out.")
        audit_fl.write("Goodbye " + user + ", you've successfully logged out.\n")
        user = ''


def listadd(listname):
    global user
    global list_of_friends
    global list_of_names

    if user == owner:
        if listname == 'nil':
            print("Invalid input. You cannot select this name.")
            audit_fl.write("Invalid input. You cannot select this name.\n")
        elif listname not in [lst[0] for lst in list_of_names]:  # Check list names, not friends
            print(listname + " has been created!")
            audit_fl.write(listname + " has been created\n")
            list_of_names.append([listname, []])
            list_of_names.append(listname)  # Track the list name separately

            # Create a .txt file with the name of the list
            with open(listname + ".txt", "w") as file:
                file.write(f"{listname} List:\n")

        else:
            print("Invalid input. You already have a list with this name.")
            audit_fl.write("Invalid input. You already have a list with this name.\n")
    else:
        print("Invalid input. You're not root. Only root can add new lists.")
        audit_fl.write("Invalid input. You're not root. Only root can add new lists.\n")


def friendlist(friendname, listname):
    global user
    global list_of_names
    global list_of_friends

    if user == owner:
        if friendname in list_of_friends:
            # Find the correct list by its name
            list_entry = next((lst for lst in list_of_names if lst[0] == listname), None)

            if list_entry:
                if friendname in list_entry[1]:  # Check if friend is already in the list
                    print("Invalid input. " + friendname + " already exists in this list.")
                    audit_fl.write("Invalid input. " + friendname + " already exists in this list.\n")
                else:
                    list_entry[1].append(friendname)  # Append to the correct list
                    print(friendname + " has been added to your " + listname + " list.")
                    audit_fl.write(friendname + " has been added to your " + listname + " list.\n")
                    with open(listname + ".txt", "a") as file:
                        file.write(friendname + "\n")
            else:
                print("Invalid input. That list name doesn't yet exist.")
                audit_fl.write("Invalid input. That list name doesn't yet exist.\n")
        else:
            print("Invalid input. " + friendname + " isn't your friend yet.")
            audit_fl.write("Invalid input. " + friendname + " isn't your friend yet.\n")
    else:
        print("Invalid input. You are not the owner of this list.")
        audit_fl.write("Invalid input. You are not the owner of this list.\n")


def postpicture(picturename):
    global user
    global list_of_pictures

    if picturename == 'audit.txt' or picturename == 'lists.txt' or picturename == 'picture.txt':
        print("Invalid input" + picturename + " is not allowed.")
        audit_fl.write("Invalid input" + picturename + " is not allowed.\n")
    else:
        if user == '':
            print("Please log in before attempting to access this feature.")
            audit_fl.write("Please log in before attempting to access this feature.\n")
        else:
            if picturename in [pic[0] for pic in list_of_pictures]:
                print("Invalid input " + picturename + " already exists.")
                audit_fl.write("Invalid input " + picturename + " already exists.\n")
            else:
                list_of_pictures.append([picturename, user, '', ("rw", "--", "--")])
                print(user + "'s picture, " + picturename + ", has successfully been created!")
                audit_fl.write(user + "'s picture, " + picturename + ", has successfully been created!\n")
                pics = open(picturename, "w")
                pics.close()


def chlst(picturename, listname):
    global user
    global list_of_pictures

    if user == '':
        print("Please log in before attempting to access this feature.")
        audit_fl.write("Please log in before attempting to access this feature.\n")
    else:
        if picturename not in [pic[0] for pic in list_of_pictures]:
            print("Invalid input " + picturename + " doesn't exist.")
        elif (listname != 'nil') and (listname not in [lst[0] for lst in list_of_names]):
            print("Invalid input " + listname + " doesn't exist.")
            audit_fl.write("Invalid input " + listname + " doesn't\n")
        else:
            if (user != owner) and (owner != [pic[1] for pic in list_of_pictures if pic[0] == picturename][0]):
                print("Invalid input, you have to be the owner of the picture or profile.")
                audit_fl.write("Invalid input, you have to be the owner of the picture or profile.\n")
            else:
                if user == owner:
                    [pic[2] for pic in list_of_pictures if pic[0] == picturename][0] = listname
                    print(
                        user + "'s picture, " + picturename + " has successfully been added to the " + listname + " list!")
                    audit_fl.write(
                        user + "'s picture, " + picturename + ", has successfully been added to the " + listname + " list!\n")
                else:
                    if user not in [lst[1] for lst in list_of_names if lst[0] == listname][0]:
                        print("Invalid input, " + user + " has not been added to " + listname)
                        audit_fl.write("Invalid input, " + user + " has not been added to " + listname + "\n")
                    else:
                        [pic[2] for pic in list_of_pictures if pic[0] == picturename][0] = listname
                        print(
                            user + "'s picture, " + picturename + ", has successfully been added to the " + listname + " list!")
                        audit_fl.write(
                            user + "'s picture, " + picturename + ", has successfully been added to the " + listname + " list!\n")


def chmod(picturename, rw1, rw2, rw3):
    global list_of_pictures
    global user

    if picturename not in [pic[0] for pic in list_of_pictures]:
        print("Invalid input, " + picturename + " has not yet been created.")
        audit_fl.write("Invalid input, " + picturename + " has not yet been created.\n")
        return

    picture_owner = [pic[1] for pic in list_of_pictures if pic[0] == picturename][0]

    if user != owner and user != picture_owner:
        print("Invalid input, you are not the owner of the picture or profile.")
        audit_fl.write("Invalid input, you are not the owner of the picture or profile.\n")
        return

    print(user + " has set the permissions for " + picturename + " to " + rw1 + " " + rw2 + " and " + rw3)
    audit_fl.write(
        user + " has set the permissions for " + picturename + " to " + rw1 + " " + rw2 + " " + rw3 + ".\n"
    )

    for pic in list_of_pictures:
        if pic[0] == picturename:
            pic[3] = (rw1, rw2, rw3)  # Update the permissions tuple
            break


def chown(picturename, friendname):
    global user
    global list_of_pictures

    if user != owner:
        print("Invalid input, access denied. Current user: " + user + ", Owner: " + owner)
        audit_fl.write("Invalid input, access denied. Current user: " + user + ", Owner: " + owner + "\n")
        return

    if picturename not in [pic[0] for pic in list_of_pictures]:
        print("Invalid input, " + picturename + " does not exist.")
        audit_fl.write("Invalid input, " + picturename + " does not exist.\n")
        return

    if friendname not in list_of_friends:
        print("Invalid input, " + friendname + " is not your friend.")
        audit_fl.write("Invalid input, " + friendname + " is not your friend.\n")
        return

    for pic in list_of_pictures:
        if pic[0] == picturename:
            pic[1] = friendname  # Set the owner of the picture to the friend's name
            print(friendname + " is now the owner of the " + picturename + " picture.")
            audit_fl.write(friendname + " is now the owner of the " + picturename + " picture.\n")
            break

def readcomments(picturename):
    global list_of_pictures
    global user

    if user == '':
        print("Invalid input, you must be logged in to read comments.")
        audit_fl.write("Invalid input, you must be logged in to read comments.\n")
    else:
        if picturename not in [pic[0] for pic in list_of_pictures]:
            print("Invalid input, " + picturename + " does not exist.")
            audit_fl.write("Invalid input, " + picturename + " does not exist.\n")
        else:
            if (user == owner) or (
                user == [pic[1] for pic in list_of_pictures if pic[0] == picturename][0] and
                [pic[3][0] for pic in list_of_pictures if pic[0] == picturename][0].count('r') > 0
            ) or (
                [pic[2] for pic in list_of_pictures if pic[0] == picturename][0] != '' and
                user in [lst[1] for lst in list_of_names if lst[0] ==
                         [pic[2] for pic in list_of_pictures if pic[0] == picturename][0]] and
                [pic[3][1] for pic in list_of_pictures if pic[0] == picturename][0].count('r') > 0
            ) or (
                [pic[3][2] for pic in list_of_pictures if pic[0] == picturename][0].count('r') > 0
            ):
                try:
                    with open(picturename, "r") as file:  # Open the correct file
                        lines = file.readlines()
                        print(user + " reads " + picturename + " as: ")
                        audit_fl.write(user + " reads " + picturename + " as: \n")

                        for line in lines:
                            print(line, end='')
                            audit_fl.write(line)
                except FileNotFoundError:
                    print("Error: File for " + picturename + " does not exist.")
                    audit_fl.write("Error: File for " + picturename + " does not exist.\n")
            else:
                print(user + " has denied your read access request to " + picturename)
                audit_fl.write(user + " has denied your read access request to " + picturename + '\n')

def writecomments(picturename, text):
    global pictures_fl
    global user
    global first_word
    global list_of_pictures

    if user == '':
        print("Invalid input, you must be logged in to write comments.")
        audit_fl.write("Invalid input, you must be logged in to write comments.\n")
    else:
        if picturename not in [pic[0] for pic in list_of_pictures]:
            print("Invalid input, " + picturename + " does not exist.")
            audit_fl.write("Invalid input, " + picturename + " does not exist.\n")
        else:
            if (user == owner) or (user == [pic[1] for pic in list_of_pictures if pic[0] == picturename][0] and
                                   [pic[3][0] for pic in list_of_pictures if pic[0] == picturename][0].count(
                                       'w') > 0) or (
                    [pic[2] for pic in list_of_pictures if pic[0] == picturename][0] != '' and
                    user in [lst[1] for lst in list_of_names if
                             lst[0] == [pic[2] for pic in list_of_pictures if pic[0] == picturename][0]] and
                    [pic[3][1] for pic in list_of_pictures if pic[0] == picturename][0].count('w') > 0) or (
                    [pic[3][2] for pic in list_of_pictures if pic[0] == picturename][0].count('w') > 0):
                print(user + " commented on " + picturename + ": " + text)
                audit_fl.write(user + " commented on " + picturename + ": " + text + '\n')
                file = open(picturename, 'a')
                file.write(text + '\n')
            else:
                if first_word:
                    print(user + " denied your access to " + picturename + ": " + text)
                    audit_fl.write(user + " denied your access to " + picturename + ": " + text + '\n')
                    first_word = False


def end():
    global lists_fl
    global pictures_fl

    audit_fl.close()
    lists_fl = open('lists.txt', 'w')
    for lst in list_of_names:
        lists_fl.write(": ".join(map(str, lst)) + '\n')
    lists_fl.close()

    pictures_fl = open('picture.txt', 'w')
    pictures_fl.write(json.dumps(list_of_pictures))
    pictures_fl.close()


def main():
    global audit_fl
    global lists_fl
    global pictures_fl
    global line_ct
    audit_fl = open('audit.txt', 'w')
    friends_fl = open('friends.txt', 'w')
    friends_fl.close()
    user_input = sys.argv
    file = open(user_input[1], 'r')
    lines = file.readlines()
    file.close()

    for l in range(line_ct, len(lines)):
        cmd = lines[l].split()
        line_ct = line_ct + 1
        commands(cmd)


main()
