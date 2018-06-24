from sys import argv
from os.path import exists

script, user_name, from_file, to_file = argv

print "Hello, %s?" % (user_name)
print "We're going to do some few simple things,If thats okay with you, hit RETURN."
raw_input()

print "Opening the file..."
in_file = open(from_file, 'w' )

print "Deleting the file..."
in_file.truncate()

print "I'm going to ask you for some few lines."
print "If you will allow it hit RETURN"
raw_input()

line1 = raw_input(": ")
line2 = raw_input(": ")
line3 = raw_input(": ")


print "Now I'm going to print this into the file."

in_file.write(line1 + '\n' + line2 + '\n' + line3 + '\n')

in_file.close()

print "Now with your permision can I copy this to another file %s?" % (to_file)
print "Hit RETURN if thats okay."
raw_input()

print "Firstly,does the file exist? %s " % exists(to_file)
print "Opening the file..."

out_file = open(to_file, 'w')

print "Deleting what's in the file..."
out_file.truncate()

print "Copying the files..."
in_file = open(from_file)
indata = in_file.read()
out_file.write(indata)

print "Thank you for your service."

out_file.close()
in_file.close()



