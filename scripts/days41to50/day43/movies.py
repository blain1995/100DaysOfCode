from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text

soup = BeautifulSoup(data, "html.parser")

movies = soup.find_all(target="_self")
movie_names = [movie.string.split("Read Empire's review of")[1].strip() for movie in movies if len(movie.string.split("Read Empire's review of"))> 1]
movie_names.reverse()
print(movie_names)

number = 1

with open("movies.txt", "w") as file:
    for movie in movie_names:
        file.write(f"{number}) {movie}\n")
        number += 1

