annual_fee = int(input())

basketball_shoes = annual_fee * 0.60
basketball_team = basketball_shoes * 0.80
basketball = basketball_team * 0.25
basketball_accessories = basketball * 0.20

total_price = (annual_fee
               + basketball_shoes
               + basketball_team
               + basketball
               + basketball_accessories)
print(f'{total_price:.2f}')
