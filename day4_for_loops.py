item_list = ['Oak Wood', 'Blue Paint', 'White Paint', 'Paint Finish']

amount_list = [600, 150, 15, 165]

wholesale_price_list = [7000, 1000, 1000, 800]

retail_price = [12.99, 8.99, 9.99, 3.99]

retail_oak = 0
retail_blue_paint = 0
retail_white_paint = 0
retail_paint_finish = 0

for i in range(amount_list[0]):
    retail_oak = retail_oak + retail_price[0]
    if (retail_oak > wholesale_price_list[0]):
        retail_oak = wholesale_price_list[0]

for i in range(amount_list[1]):
    retail_blue_paint = retail_blue_paint + retail_price[1]
    if (retail_blue_paint > wholesale_price_list[1]):
        retail_blue_paint = wholesale_price_list[1]

for i in range(amount_list[2]):
    retail_white_paint = retail_white_paint + retail_price[2]
    if (retail_white_paint > wholesale_price_list[2]):
        retail_white_paint = wholesale_price_list[2]

for i in range(amount_list[3]):
    retail_paint_finish = retail_paint_finish + retail_price[3]
    if (retail_paint_finish > wholesale_price_list[3]):
        retail_paint_finish = wholesale_price_list[3]

print(retail_oak, retail_blue_paint, retail_white_paint, retail_paint_finish)

# answer is yes, yes, no, no
