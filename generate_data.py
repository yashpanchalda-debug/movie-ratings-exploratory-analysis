"""
generate_data.py
Generates a synthetic movie ratings dataset and saves it to movies.csv.
"""

import numpy as np
import pandas as pd

np.random.seed(42)

NUM_MOVIES = 500

GENRES = ["Action", "Comedy", "Drama", "Horror", "Romance", "Sci-Fi", "Documentary", "Thriller"]

# Genre biases: some genres tend to rate higher
GENRE_RATING_BIAS = {
    "Action": 0.0,
    "Comedy": 0.2,
    "Drama": 0.5,
    "Horror": -0.3,
    "Romance": 0.1,
    "Sci-Fi": 0.3,
    "Documentary": 0.6,
    "Thriller": 0.2,
}

def generate_title(i, genre):
    adjectives = ["Lost", "Dark", "Eternal", "Broken", "Silent", "Hidden", "Burning", "Frozen"]
    nouns = ["World", "Dream", "Shadow", "Echo", "Storm", "Journey", "Legacy", "Signal"]
    return f"The {adjectives[i % len(adjectives)]} {nouns[(i + 3) % len(nouns)]} {i + 1}"

years = np.random.choice(range(1980, 2024), size=NUM_MOVIES, p=None)

# Weight years so recent years have more movies
year_weights = np.array([1 + (y - 1980) * 0.15 for y in range(1980, 2024)])
year_weights = year_weights / year_weights.sum()
years = np.random.choice(range(1980, 2024), size=NUM_MOVIES, p=year_weights)

genres = np.random.choice(GENRES, size=NUM_MOVIES)

ratings = np.array([
    round(np.clip(np.random.normal(6.5 + GENRE_RATING_BIAS[g], 1.2), 1.0, 10.0), 1)
    for g in genres
])

votes = np.random.randint(500, 500000, size=NUM_MOVIES)
runtimes = np.random.randint(75, 180, size=NUM_MOVIES)

titles = [generate_title(i, genres[i]) for i in range(NUM_MOVIES)]

df = pd.DataFrame({
    "title": titles,
    "genre": genres,
    "year": years,
    "rating": ratings,
    "votes": votes,
    "runtime_min": runtimes,
})

df.to_csv("movies.csv", index=False)
print(f"Dataset saved to movies.csv ({len(df)} movies)")
print(df.head())