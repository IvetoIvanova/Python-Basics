desired_profit = float(input())

club_income = 0
is_party = False
target_acquired = False

while True:
    data = input()

    if data == 'Party!':
        is_party = True
        break

    cocktails_number = int(input())

    cocktail_price = len(data)
    current_sum = cocktails_number * cocktail_price

    if current_sum % 2 != 0:
        current_sum -= current_sum * 0.25

    club_income += current_sum

    if desired_profit <= club_income:
        target_acquired = True
        break

if is_party:
    needed_sum = desired_profit - club_income
    print(f'We need {needed_sum:.2f} leva more.')
elif target_acquired:
    print('Target acquired.')

print(f'Club income - {club_income:.2f} leva.')
