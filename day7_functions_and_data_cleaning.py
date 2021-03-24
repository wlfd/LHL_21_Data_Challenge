import pandas as pd

#example dicitonary
user_boxes = {
    'weight': [4, 2, 18, 21, 14, 13],
    'box_name': ['box1', 'box2', 'box3', 'box4', 'box5', 'box6']
}

print(pd.DataFrame(user_boxes).sort_values('weight'))

# def sort(b):
#   if len(b['weight']) == 1:
#     return [b['box_name'][0]]

#   min_i = 0

#   for i in range(len(b['weight'])):
#     if (b['weight'][i] < b['weight'][min_i]):
#       min_i = i

#   sorted_boxes = b['box_name'][min_i]
#   b['weight'].pop(min_i)
#   b['box_name'].pop(min_i)
#   return [sorted_boxes] + sort(b)

# print(sort(user_boxes)) # changes user_boxes
# print(user_boxes)

# def box_order(b):
#   l = b['weight']
#   b = b['box_name']
#   for i in range(len(l)):
#       for j in range(i + 1, len(l)):
#           if l[i] > l[j]:
#               l[i], l[j] = l[j], l[i] # swap 'weight'
#               b[i], b[j] = b[j], b[i] # swap 'box_name'

# box_order(user_boxes)
# print(user_boxes)


def insertionSort(b):
  for i in range(len(b['weight'])):
    curr_w = b['weight'][i]
    curr_b = b['box_name'][i]
    # shift elements in b[0..i-1], that are
    # greater than curr_w, to one position ahead
    # of their current position
    j = i - 1

    while (j >= 0 and curr_w < b['weight'][j]):
      b['weight'][j + 1] = b['weight'][j] # swap b['weight']
      b['box_name'][j + 1] = b['box_name'][j] # swap b['box_name']
      j -= 1

    b['weight'][j + 1] = curr_w
    b['box_name'][j + 1] = curr_b


insertionSort(user_boxes)
print(user_boxes)

# zip?? lambda??
