import math

num_of_guests = int(input())
budget = int(input())

num_of_cozunas = math.ceil(num_of_guests / 3)
num_of_eggs = num_of_guests * 2

final_price = (num_of_cozunas * 4) + (num_of_eggs * 0.45)

if budget >= final_price:
    money_left = budget - final_price
    print(f'Lyubo bought {num_of_cozunas} Easter bread and {num_of_eggs} eggs.')
    print(f'He has {money_left:.2f} lv. left.')
else:
    needed_money = final_price - budget
    print('Lyubo doesn\'t have enough money.')
    print(f'He needs {needed_money:.2f} lv. more.')
