balance = -1
checkBalance = False
isActive = True

if not(checkBalance):
    print "Thank you.Have a nice day!"
elif isActive and balance > 0:
    print "Your balance is $", balance
elif not(isActive):
    print "Your account is no longer active."
elif balance == 0:
    print "Your account is empty."
else:
    print "Your balance is negative.\nPlease contact bank."
