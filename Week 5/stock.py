import random

MAX_INCREASE=0.175
MAX_DECREASE=0.05
MIN_PRICE=0.01
MAX_PRICE=100.0
INITIAL_PRICE=10.0


def convert(price):
    converted=("${:,.2f}".format(price))
    return converted

price = INITIAL_PRICE
print("Starting price:",convert(price))
day=0
while price >= MIN_PRICE and price <= MAX_PRICE:
    priceChange = 0
    if random.randint(1, 2)== 1:
        priceChange = random.uniform(0, MAX_INCREASE)
    else:
        priceChange = random.uniform(--MAX_DECREASE,0)
    day+=1
    price *= (1 + priceChange)
    print("On day {} price is:".format(day),convert(price))
