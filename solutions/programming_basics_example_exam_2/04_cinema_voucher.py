voucher_value = int(input())
ticket_counter = 0
other_purchases_counter = 0

while True:
    purchase = input()

    if purchase == 'End':
        break

    if len(purchase) > 8:
        purchase_price = ord(purchase[0]) + ord(purchase[1])
    else:
        purchase_price = ord(purchase[0])

    if purchase_price <= voucher_value:
        voucher_value -= purchase_price
        if len(purchase) > 8:
            ticket_counter += 1
        else:
            other_purchases_counter += 1
    else:
        break

print(f'{ticket_counter}')
print(f'{other_purchases_counter}')
