destination = input()
dates = input()
num_of_nights = int(input())

total_sum = 0.0

if destination == 'France':
    if dates == '21-23':
        total_sum = num_of_nights * 30
    elif dates == '24-27':
        total_sum = num_of_nights * 35
    elif dates == '28-31':
        total_sum = num_of_nights * 40
elif destination == 'Italy':
    if dates == '21-23':
        total_sum = num_of_nights * 28
    elif dates == '24-27':
        total_sum = num_of_nights * 32
    elif dates == '28-31':
        total_sum = num_of_nights * 39
elif destination == 'Germany':
    if dates == '21-23':
        total_sum = num_of_nights * 32
    elif dates == '24-27':
        total_sum = num_of_nights * 37
    elif dates == '28-31':
        total_sum = num_of_nights * 43

print(f'Easter trip to {destination} : {total_sum:.2f} leva.')
