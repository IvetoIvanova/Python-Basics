number_of_windows = int(input())
type_of_frames = input()
method_of_receipt = input()

total_price = 0.0

if number_of_windows < 10:
    print('Invalid order')
elif number_of_windows >= 10:
    if type_of_frames == '90X130':
        total_price = 110 * number_of_windows
        if number_of_windows > 60:
            total_price -= total_price * 0.08
        elif number_of_windows > 30:
            total_price -= total_price * 0.05
    elif type_of_frames == '100X150':
        total_price = 140 * number_of_windows
        if number_of_windows > 80:
            total_price -= total_price * 0.10
        elif number_of_windows > 40:
            total_price -= total_price * 0.06
    elif type_of_frames == '130X180':
        total_price = 190 * number_of_windows
        if number_of_windows > 50:
            total_price -= total_price * 0.12
        elif number_of_windows > 20:
            total_price -= total_price * 0.07
    elif type_of_frames == '200X300':
        total_price = 250 * number_of_windows
        if number_of_windows > 50:
            total_price -= total_price * 0.14
        elif number_of_windows > 25:
            total_price -= total_price * 0.09

    if method_of_receipt == 'With delivery':
        total_price += 60
    elif method_of_receipt == 'Without delivery':
        pass

    if number_of_windows >= 100:
        total_price -= total_price * 0.04

    print(f'{total_price:.2f} BGN')
