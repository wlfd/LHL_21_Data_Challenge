old_blueprint = {
    "Kitchen": ['Dirty', 'Oak', "Damaged", "Green"],
    "Dining Room": ['Dirty', 'Pine', 'Good Condition', 'Grey'],
    "Living Room": ['Dirty', 'Oak', 'Damaged', 'Red'],
    "Bedroom": ["Clean", 'Mahogany', 'Good Condition', 'Green'],
    "Bathroom": ["Dirty", 'White Tile', 'Good Condition', 'White'],
    "Shed": ['Dirty', "Cherry", "Damaged", "Un-painted"]
    # 6 rooms
    # 2 rooms need Oak and are damaged -> 20 x Oak Plank per room
    # 1 room need Cherry and is damaged -> 20 x Cherry Plank per room
    # 1 room is un-painted -> needs 3 White Paint
}

shopping_list = [
    '20 x Oak Plank', '20 x Oak Plank', '20 x Cherry Plank', 'White Paint',
    'White Paint', 'White Paint'
]

# Dot has some specific rules for what they want to change in the shopping list:
# They hate oak wood, and prefer maple.
# They want to paint all the rooms blue except the kitchen, which they want to paint white.


new_shopping_list = {}
paint_list = new_shopping_list[3:]  # does not include index 3

list = [1, 2, 3, 4, 5]
list[1:4]  # Print the range between index position 1 to before 4. Output will be [2,3,4]
list[1:5]  # Print the range between index position 1 to before 5. Output will be [2,3,4,5]
list[1:]  # Print the range between index position 1 to the end. Output will be the [2,3,4,5]
list[:2]  # Print the range between index position 0 to before 2. Output will be [1,2]

print(paint_list)
