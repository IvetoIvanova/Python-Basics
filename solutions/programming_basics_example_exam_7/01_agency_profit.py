airline_name = input()
num_of_tickets_for_adults = int(input())
num_of_tickets_for_children = int(input())
net_price_of_adult_ticket = float(input())
price_of_service_charge = float(input())

price_of_child_ticket = net_price_of_adult_ticket * 0.30
total_price_of_tickets_for_adults = (net_price_of_adult_ticket + price_of_service_charge) * num_of_tickets_for_adults
total_price_of_tickets_for_children = (price_of_child_ticket + price_of_service_charge) * num_of_tickets_for_children
total_price_for_all_tickets = total_price_of_tickets_for_children + total_price_of_tickets_for_adults

agency_profit = total_price_for_all_tickets * 0.20
print(f'The profit of your agency from {airline_name} tickets is {agency_profit:.2f} lv.')
