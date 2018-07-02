prices={
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock ={
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

total=0.0
for fruit in prices:
    print(fruit)
    print("Price : {}".format(prices[fruit]))
    print("Stock : {}".format(stock[fruit]))
    
    total += prices[fruit]*stock[fruit]
    
    print(prices[fruit]*stock[fruit])
    print()

print("Total : {}".format(total))    