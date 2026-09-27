from bisect import bisect_left

prices = [100, 200, 300, 500, 700]
new_price = 400

position = bisect_left(prices, new_price)

prices.insert(position, new_price)

print("Insertion Position:", position)
print("Updated Prices:", prices)