# using greedy algorithm

def profit(stock_prices):

    if len(stock_prices) < 2:
        raise ValueError("stock prices can't be less than 2'")

    min_stock_price = stock_prices[0]
    max_profit = stock_prices[1] - min_stock_price

    for price in stock_prices[1:]:
        comparison_price = price - min_stock_price
        max_profit = max(max_profit, comparison_price)
        min_stock_price = min(min_stock_price, price)

    return max_profit


print(profit([23, 12, 3, 10, 7, 6, 13, 11, 9, 15, 2]))

print(profit([23, 12, 10, 7, 5, 4, 2]))

print(profit([23, 3]))
