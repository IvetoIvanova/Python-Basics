projection = input()
movie_pack = input()
tickets_number = int(input())

total_price = 0

if projection == 'John Wick':
    if movie_pack == 'Drink':
        total_price = 12
    elif movie_pack == 'Popcorn':
        total_price = 15
    elif movie_pack == 'Menu':
        total_price = 19
elif projection == 'Star Wars':
    if movie_pack == 'Drink':
        total_price = 18
    elif movie_pack == 'Popcorn':
        total_price = 25
    elif movie_pack == 'Menu':
        total_price = 30
elif projection == 'Jumanji':
    if movie_pack == 'Drink':
        total_price = 9
    elif movie_pack == 'Popcorn':
        total_price = 11
    elif movie_pack == 'Menu':
        total_price = 14

total_price *= tickets_number

if projection == 'Star Wars' and tickets_number >= 4:
    total_price *= 0.70
elif projection == 'Jumanji' and tickets_number == 2:
    total_price *= 0.85

print(f'Your bill is {total_price:.2f} leva.')
