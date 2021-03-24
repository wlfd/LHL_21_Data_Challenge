import random
import pandas as pd

random.seed(34) # base number to generate random numbers

hole_sizes = [random.randint(1,i) for i in range (1, 101)]
random.shuffle(hole_sizes)

# print(hole_sizes[0:])
series_sizes = pd.Series(hole_sizes)
print('Average hole size:', round(series_sizes.mean(),2) , 'mm')

total_cost = 0
for i in range(len(hole_sizes)):
  if (hole_sizes[i] < 20):
    total_cost += 1.30
  elif (hole_sizes[i] >= 70):
    total_cost += 2.10
  else:
    total_cost += 1.60

print('Average cost: $', round(total_cost/len(hole_sizes), 3))
print('Total cost: $', round(total_cost, 3))

# hole_prices = []
# for i in range(len(hole_sizes)):
#     if hole_sizes[i] < 20:
#         hole_prices.append(1.30)
#     elif hole_sizes[i] >= 20 and hole_sizes[i] < 70:
#         hole_prices.append(1.6)
#     else:
#         hole_prices.append(2.10)
# price_series = pd.Series(hole_prices)
# print(f"Average cost to fix a hole is {price_series.mean()}")
# print(f"Total cost to fix all holes is {sum(hole_prices)}")
# print(f"Max size hole is {series.min()}")
# print(f"Min size hole is {series.max()}")