movie_name = input()
num_of_days = int(input())
tickets_num = int(input())
ticket_price = float(input())
percentage_for_cinema = int(input())

tickets_price_per_day = tickets_num * ticket_price
tickets_price_for_all_days = num_of_days * tickets_price_per_day
cinema_income = tickets_price_for_all_days * (percentage_for_cinema / 100)
movie_profit = tickets_price_for_all_days - cinema_income

print(f'The profit from the movie {movie_name} is {movie_profit:.2f} lv.')
