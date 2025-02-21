capacity = int(input())

is_movie_time = False
full_cinema = False
cinema_income = 0

while True:
    data = input()

    if data == 'Movie time!':
        is_movie_time = True
        break

    number_of_people = int(data)

    if capacity < number_of_people:
        full_cinema = True
        break

    cinema_income += number_of_people * 5

    if number_of_people % 3 == 0:
        cinema_income -= 5

    capacity -= number_of_people

if is_movie_time:
    print(f'There are {capacity} seats left in the cinema.')
elif full_cinema:
    print('The cinema is full.')

print(f'Cinema income - {cinema_income} lv.')
