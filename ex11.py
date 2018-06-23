print "How old are you?", # the commas is so that the input does not go to the next line.
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you're %r old, %r tall, and %r heavy." % (
	age, height, weight)


# raw_input takes the input changes it and puts in the new input.