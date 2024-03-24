import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="ISS"
)
user_db = db.cursor()

genres_input = input("Enter genres to search for: ")
genres = [genre.title() for genre in genres_input.split()]

rating_input = input("Enter rating limits: ")
ratings = [float(item) for item in rating_input.split()]

episode_input = input("Enter episode count limits: ")
episodes = [int(item) for item in episode_input.split()]

genre_conditions = ' OR '.join([f'genres LIKE "%{genre}%"' for genre in genres])
rating_condition = f'rating >= {ratings[0]} and rating <= {ratings[1]}'
episode_condition = f'num_episodes >= {episodes[0]} and num_episodes <= {episodes[1]}'

query = f'SELECT * FROM shows WHERE {genre_conditions} and {rating_condition} and {episode_condition};'
user_db.execute(query)
results = user_db.fetchall()

result_dict = {row[1]: float(row[2]) for row in results}

for row in results:
    print(row)
    result_dict[row[1]] = float(row[2])

db.close()
