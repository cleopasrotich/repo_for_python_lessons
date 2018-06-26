def print_two(*args):
	arg1,arg2 = args
	print "arg1: %s, arg2: %s" % (arg1, arg2)


def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)


def print_one(arg1):
	print "arg1: %r" % arg1


def print_none():
	print "I got nothin'"


print_two("Cleopas","Rotich")
print_two_again("Cleopas", "Rotich")
print_one("I love python")
print_none()	

# we first tell python to make a function using define.
# never forget to put a semi colon