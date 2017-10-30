def scoreGrades():
    print "Scores and Grades"
    import random
    generates = 10
    while generates > 0:
        generates -= 1
        score = random.randint(60,100)
        if score > 60 and score < 69:
            print "Score: " + str(score) + "; " + "Your grade is D"
        elif score > 70 and score < 79:
            print "Score: " + str(score) + "; " + "Your grade is C"
        elif score > 80 and score < 89:
            print "Score: " + str(score) + "; " + "Your grade is B"
        else:
            print "Score: " + str(score) + "; " + "Your grade is B" 
    return "End of the program. Bye!"

print scoreGrades()