def numbers(limit):
    i = 0
    numbers = []

    while i < limit:
        print "At the top is %r" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now:", numbers
        print "At the botom is %r" % i

    print numbers

user_limit = int(raw_input("Give me a limit: "))
numbers(user_limit)

def numbers(limit):
    numbers = []

    for i in range(limit):
        print "At the top is %r" % i
        numbers.append(i)
        print numbers
        


user_limit = int(raw_input("Add your number "))
numbers(user_limit)
