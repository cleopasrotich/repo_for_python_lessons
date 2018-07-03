print "You enter a dark room with two doors. Do you go through door #1 or door #2."

door = raw_input("> ")

if door == "1":
    print "There's a large giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Screem at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear comes to you with fury."
        print "There is a knife to the left and a gun to the right."
        print "Which one do you go for?"

        pick = raw_input("> ")

        if pick == "knife":
            print "The bear charges at you but you dogde it and You chop off its head."
        elif pick == "gun":
            print "You reach for the gun as the bear charges at you but when you pull the trigger you find out it has no bullets."
            print "The bear then rips you apart ."
        else:
            print "Try to pet the bear."

    elif bear == "2":
        print "The bear eats your legs off.Good job."
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolving ending melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job."
    else:
        print "The insanity rots your eyes into a pool of muck."

else:
    print "You stumble around and fall into a knife and die."

