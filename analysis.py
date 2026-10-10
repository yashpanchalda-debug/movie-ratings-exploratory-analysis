"""
analysis.py
Exploratory Data Analysis of the movie ratings dataset.
Generates visualizations for rating distribution, genre trends, and yearly trends.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import sys
import os

# ── Setup ──────────────────────────────────────────────────────────────────────
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams["figure.figsize"] = (10, 5)
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.labelsize"] = 12

DATA_FILE = "movies.csv"

if not os.path.exists(DATA_FILE):
    print(f"ERROR: '{DATA_FILE}' not found. Run `python generate_data.py` first.")
    sys.exit(1)

# ── Load & Inspect ─────────────────────────────────────────────────────────────
df = pd.read_csv(DATA_FILE)

print("=== Dataset Overview ===")
print(df.shape)
print(df.dtypes)
print(df.describe())
print(f"\nMissing values:\n{df.isnull().sum()}")
print(f"\nGenres: {sorted(df['genre'].unique())}")

# ── 1. Rating Distribution ─────────────────────────────────────────────────────
fig, ax = plt.subplots()
ax.hist(df["rating"], bins=20, color="steelblue", edgecolor="white", linewidth=0.6)
ax.set_title("Distribution of Movie Ratings")
ax.set_xlabel("Rating (out of 10)")
ax.set_ylabel("Number of Movies")
ax.axvline(df["rating"].mean(), color="tomato", linestyle="--", linewidth=1.5, label=f"Mean: {df['rating'].mean():.2f}")
ax.legend()
plt.tight_layout()
plt.savefig("chart_rating_distribution.png", dpi=120)
plt.show()
print("Saved: chart_rating_distribution.png")

# ── 2. Average Rating by Genre ─────────────────────────────────────────────────
genre_stats = (
    df.groupby("genre")["rating"]
    .agg(avg_rating="mean", count="count")
    .sort_values("avg_rating", ascending=False)
    .reset_index()
)

fig, ax = plt.subplots()
bars = ax.bar(genre_stats["genre"], genre_stats["avg_rating"], color=sns.color_palette("muted", len(genre_stats)))
ax.set_title("Average Rating by Genre")
ax.set_xlabel("Genre")
ax.set_ylabel("Average Rating")
ax.set_ylim(0, 10)
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%.1f"))

for bar, val in zip(bars, genre_stats["avg_rating"]):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1,
            f"{val:.2f}", ha="center", va="bottom", fontsize=9)

plt.tight_layout()
plt.savefig("chart_avg_rating_by_genre.png", dpi=120)
plt.show()
print("Saved: chart_avg_rating_by_genre.png")

print("\nGenre summary:")
print(genre_stats.to_string(index=False))

# ── 3. Movies Released per Year ────────────────────────────────────────────────
yearly_counts = df.groupby("year").size().reset_index(name="count")

fig, ax = plt.subplots()
ax.plot(yearly_counts["year"], yearly_counts["count"], marker="o", markersize=4, linewidth=1.8, color="steelblue")
ax.set_title("Number of Movies Released per Year")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Movies")
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("chart_movies_per_year.png", dpi=120)
plt.show()
print("Saved: chart_movies_per_year.png")

# ── 4. Average Rating over Time ────────────────────────────────────────────────
yearly_ratings = df.groupby("year")["rating"].mean().reset_index(name="avg_rating")

fig, ax = plt.subplots()
ax.plot(yearly_ratings["year"], yearly_ratings["avg_rating"],
        marker="o", markersize=4, linewidth=1.8, color="seagreen")
ax.set_title("Average Movie Rating by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Average Rating")
ax.set_ylim(4, 9)
ax.axhline(df["rating"].mean(), color="tomato", linestyle="--", linewidth=1.2, label=f"Overall mean: {df['rating'].mean():.2f}")
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("chart_avg_rating_by_year.png", dpi=120)
plt.show()
print("Saved: chart_avg_rating_by_year.png")

# ── 5. Top 10 Highest-Rated Movies ────────────────────────────────────────────
# Filter to movies with at least 10,000 votes for credibility
popular = df[df["votes"] >= 10000].copy()
top10 = popular.nlargest(10, "rating")[["title", "genre", "year", "rating", "votes"]]

fig, ax = plt.subplots(figsize=(10, 6))
colors = sns.color_palette("muted", len(top10))
bars = ax.barh(top10["title"], top10["rating"], color=colors)
ax.set_title("Top 10 Highest-Rated Movies (min. 10k votes)")
ax.set_xlabel("Rating")
ax.set_xlim(0, 11)
ax.invert_yaxis()

for bar, val in zip(bars, top10["rating"]):
    ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height() / 2,
            f"{val:.1f}", va="center", fontsize=9)

plt.tight_layout()
plt.savefig("chart_top10_movies.png", dpi=120)
plt.show()
print("Saved: chart_top10_movies.png")

print("\nTop 10 highest-rated movies (min. 10k votes):")
print(top10.to_string(index=False))

# ── Summary Statistics ─────────────────────────────────────────────────────────
print("\n=== Final Summary ===")
print(f"Total movies analysed : {len(df)}")
print(f"Year range            : {df['year'].min()} – {df['year'].max()}")
print(f"Rating range          : {df['rating'].min()} – {df['rating'].max()}")
print(f"Mean rating           : {df['rating'].mean():.2f}")
print(f"Median rating         : {df['rating'].median():.2f}")
print(f"Most common genre     : {df['genre'].value_counts().idxmax()}")