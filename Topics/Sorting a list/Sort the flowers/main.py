# the following line creates a list from the input, do not modify it, please
prices = [float(price) for price in input().split()]

# your code below
print([x for x in reversed(sorted(prices))])
