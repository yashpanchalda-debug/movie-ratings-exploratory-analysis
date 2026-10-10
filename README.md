# Movie Ratings Exploratory Analysis

An exploratory data analysis (EDA) project examining movie ratings trends using Python, Pandas, and Matplotlib. This project covers rating distributions, genre breakdowns, and yearly trends.

## Project Structure

```
movie-ratings-eda/
├── README.md
├── generate_data.py       # Script to generate sample dataset
├── analysis.py            # Main EDA script with visualizations
├── requirements.txt       # Python dependencies
```

## What This Project Demonstrates

- Data loading and cleaning with **Pandas**
- GroupBy aggregations and pivot operations
- Data visualization with **Matplotlib** and **Seaborn**
- Exploratory analysis workflow: distributions, trends, comparisons

## Setup & Usage

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Generate the sample dataset

```bash
python generate_data.py
```

This creates `movies.csv` in the project directory.

### 3. Run the analysis

```bash
python analysis.py
```

This will display several charts:
- Rating distribution histogram
- Average rating by genre (bar chart)
- Number of movies released per year (line chart)
- Average rating over time (line chart)
- Top 10 highest-rated movies (horizontal bar chart)

## Sample Insights

- Drama and Documentary genres tend to receive higher average ratings
- Movie output increased significantly from the 1990s onward
- Ratings cluster around 6–7.5 on a 10-point scale

## Requirements

- Python 3.8+
- pandas
- matplotlib
- seaborn
- numpy

## Dataset

The dataset is synthetically generated for demonstration purposes and includes ~500 movies with fields: title, genre, year, rating, votes, and runtime.