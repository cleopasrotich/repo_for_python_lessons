people = 30 
cars = 40 
buses = 15


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should take the bus."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the bus."
else:
    print "It's still a difficult decision."

if people > buses:
    print "Alright, lets just take the bus."
else:
    print "Lets just stay."