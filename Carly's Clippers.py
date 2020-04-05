"""
You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. Your job is to go through
the lists of data that have been collected in the past couple of weeks. You will be calculating some
important metrics that Carly can use to plan out the operation of the business for the rest of the month.
"""

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

average_price = 0
total_price = 0
total_revenue = 0
new_prices = []

for price in prices:
    total_price = total_price + price
    average_price += total_price / len(prices)

for price in prices:
    new_price = price - 5
    new_prices.append(new_price)

for i in range(len(hairstyles)):
    total_revenue += (prices[i] * last_week[i])

# print(total_price)
print("Average Haircut Price: " + str(average_price))

print("New Prices are: " + str(new_prices))
print("Total Revenue: " + str(total_revenue))

average_daily_revenue = total_revenue / 7
print("Daily Revenue: " + str(average_daily_revenue))

cuts_under_30 = []

for i in range(len(hairstyles)):
    if new_prices[i] < 30:
        cuts_under_30.append(hairstyles[i])

print(cuts_under_30)

