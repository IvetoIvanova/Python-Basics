customers_count = int(input())

total_revenue = 0

for _ in range(customers_count):
    total_price = 0
    items_count = 0

    while True:
        item = input()

        if item == "Finish":
            break

        items_count += 1

        if item == "basket":
            total_price += 1.50
        elif item == "wreath":
            total_price += 3.80
        elif item == "chocolate bunny":
            total_price += 7.00

    if items_count % 2 == 0:
        total_price *= 0.80

    total_revenue += total_price
    print(f"You purchased {items_count} items for {total_price:.2f} leva.")

average_bill = total_revenue / customers_count
print(f"Average bill per client is: {average_bill:.2f} leva.")
