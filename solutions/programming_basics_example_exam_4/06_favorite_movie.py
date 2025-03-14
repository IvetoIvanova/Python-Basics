best_movie = ""
best_score = 0
movie_count = 0

while movie_count < 7:
    movie_title = input()

    if movie_title == "STOP":
        break

    movie_count += 1
    score = 0

    for char in movie_title:
        score += ord(char)

        if char.islower():
            score -= 2 * len(movie_title)
        elif char.isupper():
            score -= len(movie_title)

    if score > best_score:
        best_score = score
        best_movie = movie_title

    if movie_count == 7:
        print("The limit is reached.")
        break

print(f"The best movie for you is {best_movie} with {best_score} ASCII sum.")
