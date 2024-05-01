absent = [2,5]

for student in range (1,11): #1, 10
    if student in absent:
        continue
    print ("{0}, 책을 읽어줘".format(student))
    