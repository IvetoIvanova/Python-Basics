amount_of_eggs = int(input())
sold_eggs = 0

while True:
    command = input()

    if command == 'Close':
        print('Store is closed!')
        print(f'{sold_eggs} eggs sold.')
        break

    number_of_eggs = int(input())

    if command == 'Buy':
        if amount_of_eggs < number_of_eggs:
            print('Not enough eggs in store!')
            print(f'You can buy only {amount_of_eggs}.')
            break
        else:
            amount_of_eggs -= number_of_eggs
            sold_eggs += number_of_eggs
    elif command == 'Fill':
        amount_of_eggs += number_of_eggs
