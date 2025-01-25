import math

tennis_racket_price = int(input())
num_of_tennis_rackets = int(input())
num_of_sneakers = int(input())

total_price_of_rackets = tennis_racket_price * num_of_tennis_rackets
total_price_of_sneakers = (tennis_racket_price / 6) * num_of_sneakers
other_equipment = (total_price_of_rackets + total_price_of_sneakers) * 0.2
total_price = total_price_of_rackets + total_price_of_sneakers + other_equipment

price_for_djokovic = total_price / 8
price_for_sponsors = total_price * (7 / 8)

print(f'Price to be paid by Djokovic {math.floor(price_for_djokovic)}')
print(f'Price to be paid by sponsors {math.ceil(price_for_sponsors)}')
