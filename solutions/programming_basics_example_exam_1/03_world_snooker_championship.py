stage_championship = input()
type_of_ticket = input()
number_of_tickets = int(input())
trophy_photo = input()

tickets_price = 0

if stage_championship == "Quarter final":
    if type_of_ticket == "Standard":
        tickets_price = 55.50 * number_of_tickets
    elif type_of_ticket == "Premium":
        tickets_price = 105.20 * number_of_tickets
    elif type_of_ticket == "VIP":
        tickets_price = 118.90 * number_of_tickets

elif stage_championship == "Semi final":
    if type_of_ticket == "Standard":
        tickets_price = 75.88 * number_of_tickets
    elif type_of_ticket == "Premium":
        tickets_price = 125.22 * number_of_tickets
    elif type_of_ticket == "VIP":
        tickets_price = 300.40 * number_of_tickets

elif stage_championship == "Final":
    if type_of_ticket == "Standard":
        tickets_price = 110.10 * number_of_tickets
    elif type_of_ticket == "Premium":
        tickets_price = 160.66 * number_of_tickets
    elif type_of_ticket == "VIP":
        tickets_price = 400 * number_of_tickets

if 2500 < tickets_price <= 4000:
    tickets_price = tickets_price * 0.90
    if trophy_photo == "Y":
        tickets_price += number_of_tickets * 40
elif tickets_price <= 2500 and trophy_photo == "Y":
    tickets_price += number_of_tickets * 40
elif tickets_price > 4000:
    tickets_price = tickets_price * 0.75

print(f'{tickets_price:.2f}')
