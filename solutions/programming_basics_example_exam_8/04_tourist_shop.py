budget = float(input())

product_counter = 0
total_price = 0.0

while True:
    data = input()

    if data == 'Stop':
        print(f'You bought {product_counter} products for {total_price:.2f} leva.')
        break

    product_price = float(input())
    product_counter += 1

    if product_counter % 3 == 0:
        product_price /= 2

    if product_price > (budget - total_price):
        print(f'You don\'t have enough money!')
        print(f'You need {abs(budget - total_price - product_price):.2f} leva!')
        break

    total_price += product_price
