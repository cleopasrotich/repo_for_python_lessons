the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quaters']

#this first kind of for loop goes through a list

for number in the_count:
    print "This is count %d" % number

for fruit in fruits:
    print "A fruit of type: %s" % fruit

#we can also go through mixed lists too
#note that we have to us %r because it's mixed

for i in change:
    print "I got %r" % i

#we can also build lists

elements = []

#using now the range funtion

for i in range(0, 6):
    print "Adding %d to list." % i

    elements.append(i)
    
    #append is a funtion that the list understands

for i in elements:
    print "Elements was: %d" % i


