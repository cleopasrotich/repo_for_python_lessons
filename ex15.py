from sys import argv

script, file = argv

txt = open(file)

print "Here's your file %r:" % (file)
print txt.read()

print "Type the file again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()