aList = ["This is a list", "rigth"]
aTuple = ("This is a tuple", "right")

icandothistoatuple = aTuple * 4

print("Can i multiply lists?")

if len(aList) * 4 == len(list(icandothistoatuple)):
    print("Yes you can multiply lists, the same way of tuples")
else:
    print("No you really cant, or you can but there are some flaws in the code maybe the = should be === or maybe im just dumb enoug not to relize that \" This is a tuple\" is definetly different than \"This is a list\" ")