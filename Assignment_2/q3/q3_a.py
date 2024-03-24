from bs4 import BeautifulSoup
import requests
import re
import matplotlib.pyplot as plt
from collections import Counter
import mysql.connector

url = 'https://www.imdb.com/chart/toptv/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
response = requests.get(url, headers=headers)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")

response_status = response.status_code

movies = soup.find_all(class_='ipc-title__text')
ratings = soup.find_all(class_='ipc-rating-star')

movie_list = [i.get_text() for i in movies[2:-12]]
ratings_list = [i.get_text().split("\xa0") for i in ratings[::2]]
num_ratings = [rating[1][1:-1] if len(rating) > 1 else 'N/A' for rating in ratings_list]

eps = [i.get_text() for i in soup.find_all(class_="sc-be6f1408-8 fcCUPU cli-title-metadata-item")]
ep = [int(parts[0]) for episode in eps if (parts := episode.split(' ')) and len(parts) == 2 and parts[1] == 'eps']

genre = str(soup.select('body'))
pattern = r'"titleGenres":{"genres":\[(.*?)\]'
matches = re.findall(pattern, genre, re.DOTALL)
genres = [re.findall(r'"text":"([^"]+)"', i) for i in matches]

data_list = []

for i in range(len(movie_list)):
    if i < len(ep):  # Check if the index is within the range of ep
        data = {
            "film_title": movie_list[i].split('.')[1][:50],
            "film_rating": ratings_list[i][0],
            "number_of_ratings": num_ratings[i],
            "number_of_episodes": ep[i],  # Accessing ep[i] only if it's within the range
            "film_genre": genres[i]
        }
        data_list.append(data)
    else:
        print("Number of episodes not available for:", movie_list[i])
        # Handle this case according to your requirements, e.g., assign a default value

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="ISS"
)
user_db = db.cursor()

sql_delete = "DELETE FROM shows"
user_db.execute(sql_delete)
db.commit()

for data in data_list:
    title = str(data["film_title"])
    rating = str(data["film_rating"])
    num_ratings = str(data["number_of_ratings"])
    num_episodes = str(data["number_of_episodes"])
    genre = ','.join(data["film_genre"])

    count_command = "SELECT COUNT(id) FROM shows;"
    user_db.execute(count_command)
    count = str(user_db.fetchone()[0] + 1)

    # Insert data into table
    insert_sql = "INSERT INTO shows (id, title, rating, num_episodes, num_ratings, genres) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(count, title, rating, num_episodes, num_ratings, genre)
    user_db.execute(insert_sql)

db.commit()

# Plot bar graph
user_db.execute("SELECT genres FROM shows")
genre_data = user_db.fetchall()
individual_genres = [genre.strip() for genres_str in genre_data for genre in genres_str[0].split(',')]
genre_counts = Counter(individual_genres)

genres = list(genre_counts.keys())
counts = list(genre_counts.values())

plt.figure(figsize=(10, 6))
plt.bar(genres, counts, color='skyblue')
plt.xlabel('Genres')
plt.ylabel('Number of TV Shows')
plt.title('Number of TV Shows by Genre')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Plot line graph
user_db.execute("SELECT num_episodes FROM shows")
episode_data = user_db.fetchall()

episodes_counts = Counter([int(episode[0]) for episode in episode_data])
num_episodes = sorted(episodes_counts.keys())
frequency = [episodes_counts[num] for num in num_episodes]

plt.figure(figsize=(10, 6))
plt.plot(num_episodes, frequency, marker='o', color='orange', linestyle='-')
plt.xlabel('Number of Episodes')
plt.ylabel('Frequency Count')
plt.title('Frequency Count of TV Shows by Number of Episodes')
plt.grid(True)
plt.tight_layout()
plt.show()
