# This  is a code for performing some operations on list.
# So lets start. As per the question in the Hackerrank.

# SOlving the list problem


# Firstly creating all the needed functions, there are 7 methods to be created

# Creating a global list to store and save values

glob_list = []
trail = []
# Creating the functions that we are using to operate

def inserting(index_position, item):
    global glob_list
    glob_list.insert(index_position, item)

def printer():
    global glob_list
    print(glob_list)

def remover(item):
    global glob_list
    glob_list.remove(item)

def appending(item):
    global glob_list
    glob_list.append(item)

def sorting():
    global glob_list
    glob_list.sort()

def poping():
    global glob_list
    glob_list.pop()

def reverser():
    global glob_list
    glob_list.reverse()


def chooser(trial):
    if trail[0] == "insert":
        if len(trail) != 3:
            print("Check the syntax")
            return
        inserting(int(trail[1]), int(trial[2]))
    if trail[0] == "print": printer()
    if trail[0] == "remove":
        if len(trial) != 2:
            print("Check the syntax")
            return
        remover(int(trail[1]))
    if trail[0] == "append":
        if len(trial) != 2:
            print("Check the syntax")
            return
        appending(int(trial[1]))
    if trail[0] == "sort": sorting()
    if trail[0] == "pop": poping()
    if trail[0] == "reverse": reverser()

# Now we have to accept the keywords from the user
print("Enter the number of commands to be executed")
inp = int(input())

for i in range(inp):
    cmd = input()
    trail = cmd.split(" ") # In this step we will get the values from the input
    chooser(trail)
