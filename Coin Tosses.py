def coinTosses():
    import random
    print "Starting the program..."
    attempt = 0
    toss = 5000
    head = 0
    tail = 0
    while toss > 0:
        attempt += 1
        toss -= 1
        chance = random.randint(1,2)
        if chance == 1:
            head += 1
            print "Attempt #" + str(attempt) + ": Throwing a coin... It's a head! ... Got " + str(head) + "(s) so far and " + str(tail) + " so far"
        else:
            tail += 1
            print "Attempt #" + str(attempt) + ": Throwing a coin... It's a tail! ... Got " + str(head) + "(s) so far and " + str(tail) + " so far"
    return "Ending the program, thank you!"

print coinTosses()