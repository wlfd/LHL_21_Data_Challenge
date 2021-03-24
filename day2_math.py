# Grocery List (19 items)
grocery_list = [
    'Bananas', 'Clementines', 'Baguette', 'Oat Milk', 'Olive Oil',
    'Coffee Beans', 'Chocolate Bar', 'Brocolli', 'Eggplant', 'Chickpeas',
    'Lentils', 'Tomatoes', 'Pasta', 'Rice', 'Yogurt', 'Blueberries', 'Onions',
    'Garlic', 'Truffles'
]

# City Price
city_price = [
    6.49, 4.99, 4.39, 4.29, 11.99, 17.99, 3.49, 3.99, 1.10, 1.99, 2.99, 4.68,
    1.59, 8.99, 3.49, 6.99, 2.99, 1.98, 14.99
]

# Country Price
country_price = [
    4.49, 4.12, 3.42, 6.99, 7.99, 14.99, 2.99, 2.49, 0.99, 1.49, 2.49, 1.99,
    1.59, 6.99, 3.89, 4.99, 1.69, 1.87, 11.49
]

sum_city_price = sum(city_price)
sum_country_price = sum(country_price)

price_difference = (sum_city_price - sum_country_price) / sum_country_price

diff = []
for i in range(len(city_price)):
    diff.append(city_price[i] - country_price[i])

diff_2 = sum(diff)/sum(country_price)

print(price_difference, diff_2)