trunk_capacity = float(input())

number_of_checked_baggage = 0
suitcase_counter = 0

while True:
    data = input()

    if data == 'End':
        print('Congratulations! All suitcases are loaded!')
        break

    suitcase_volume = float(data)
    suitcase_counter += 1

    if suitcase_counter % 3 == 0:
        suitcase_volume *= 1.10

    if suitcase_volume > trunk_capacity:
        print('No more space!')
        break
    else:
        trunk_capacity -= suitcase_volume
        number_of_checked_baggage += 1

print(f'Statistic: {number_of_checked_baggage} suitcases loaded.')
