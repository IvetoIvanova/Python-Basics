num_of_guests = int(input())
envelop_price = float(input())
budget = float(input())

final_envelopes_amount = 0.0

if 10 <= num_of_guests <= 15:
    final_envelopes_amount = envelop_price * 0.85 * num_of_guests
elif 15 < num_of_guests <= 20:
    final_envelopes_amount = envelop_price * 0.80 * num_of_guests
elif num_of_guests > 20:
    final_envelopes_amount = envelop_price * 0.75 * num_of_guests
else:
    final_envelopes_amount = envelop_price * num_of_guests

cake_price = budget * 0.10
total_sum = final_envelopes_amount + cake_price

if budget >= total_sum:
    money_left = budget - total_sum
    print(f'It is party time! {money_left:.2f} leva left.')
else:
    needed_money = total_sum - budget
    print(f'No party! {needed_money:.2f} leva needed.')
