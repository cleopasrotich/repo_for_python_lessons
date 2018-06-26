def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheese." % cheese_count
	print "You have %d crackers." % boxes_of_crackers
	print "Man that's enough for a party."
	print "Get a blanket.\n"
 
print # you then print the function with the arguments in it.
cheese_and_crackers(20, 30)


print "Or we can just use variables from our script:"
amount_cheese = 10
amount_crackers = 50

cheese_and_crackers(amount_cheese, amount_crackers)

print "We can even do math inside:"
cheese_and_crackers(10+20, 30 + 10)

print "we can combine the two variables and math:"
cheese_and_crackers(amount_cheese + 100, amount_crackers + 1000)

