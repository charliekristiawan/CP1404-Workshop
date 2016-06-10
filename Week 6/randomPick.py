import random
no_of_line = int(input("How many quick picks? "))
for i in range(no_of_line):
    data = []
    for i in range(6):
        while True:
            picks = random.randint(1, 45)
            if picks in data:
                continue
            else:
                data.append(picks)
                break
    data.sort()
    print("{:2d} {:2d} {:2d} {:2d} {:2d} {:2d}".format(data[0],data[1],data[2],data[3],data[4],data[5]))