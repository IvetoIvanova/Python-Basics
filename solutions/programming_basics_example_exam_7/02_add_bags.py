luggage_price_over_20_kg = float(input())
luggage_kilograms = float(input())
days_until_travel = int(input())
number_of_baggage = int(input())

total_price_for_baggage = 0.0
if luggage_kilograms < 10:
    total_price_for_baggage = luggage_price_over_20_kg * 0.20
elif 10 <= luggage_kilograms <= 20:
    total_price_for_baggage = luggage_price_over_20_kg * 0.50
elif luggage_kilograms > 20:
    total_price_for_baggage = luggage_price_over_20_kg

if days_until_travel < 7:
    total_price_for_baggage = total_price_for_baggage * 1.40
elif 7 <= days_until_travel <= 30:
    total_price_for_baggage = total_price_for_baggage * 1.15
elif days_until_travel > 30:
    total_price_for_baggage = total_price_for_baggage * 1.10

total_price_for_baggage = total_price_for_baggage * number_of_baggage
print(f'The total price of bags is: {total_price_for_baggage:.2f} lv.')
