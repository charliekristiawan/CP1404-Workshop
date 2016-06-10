data = []
for i in range(1,6):
    number = int(input("Number: "))
    data.append(number)

print("The first number is: {}".format(data[0]))
print("The last number is: {}".format(data[-1]))
print("The smallest number is: {}".format(min(data)))
print("The largest number is: {}".format(max(data)))
print("The average of the number is: {}".format(sum(data)/5))