import sys

movies_number = int(input())

max_rating = -sys.maxsize
min_rating = sys.maxsize
max_movie_name = ''
min_movie_name = ''
total_rating = 0

for _ in range(movies_number):
    movie_name = input()
    current_movie_rating = float(input())

    if max_rating < current_movie_rating:
        max_rating = current_movie_rating
        max_movie_name = movie_name
    if min_rating > current_movie_rating:
        min_rating = current_movie_rating
        min_movie_name = movie_name

    total_rating += current_movie_rating

average_rating = total_rating / movies_number

print(f'{max_movie_name} is with highest rating: {max_rating:.1f}')
print(f'{min_movie_name} is with lowest rating: {min_rating:.1f}')
print(f'Average rating: {average_rating:.1f}')
