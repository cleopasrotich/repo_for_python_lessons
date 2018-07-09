ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list. Lets fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()  # to pop is to add something to the list
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There is %d times now." % len(stuff)

print "There we go: ", stuff

print "Now lets do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop(6)
print ' '.join(stuff)
print '#'.join(stuff[3:5])
