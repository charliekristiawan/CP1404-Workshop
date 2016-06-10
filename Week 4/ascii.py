lower = 10
upper = 100

lhs=int(input("Enter a number ({}-{}):".format(lower,upper)).strip())
rhs=int(input("Enter a number ({}-{}):".format(lower,upper)).strip())
for i in range(lhs,rhs):
    print("{} {}".format(i, chr(i)))