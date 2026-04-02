# Vilnius Rent Analyzer

Vilnius Rent Analyzer is a web application that helps students find and compare rental apartments near VILNIUS TECH.

The app uses real housing data to support decision-making based on price, distance, and other key factors.

## Features

### Filtering
- Filter listings by:
  - maximum rent
  - distance to VILNIUS TECH
  - district
  - room type
  - furnished / unfurnished

### Sorting
- Sort results by:
  - lowest rent
  - highest rent
  - nearest distance
  - largest size

### Data Visualization
- Bar chart of average rent by district
- Scatter plot of distance vs rent

### Recommendation
- Automatically suggests top 3 properties based on:
  - rent
  - distance

### Usability
- Clickable list of property links
- Download filtered results as CSV

## Tech Stack

- Python
- pandas
- Streamlit

## Data Source

- Real housing data manually collected from:
  - Aruodas (Lithuanian real estate platform)

- Dataset includes:
  - rent (EUR)
  - distance to university (km)
  - district
  - room type
  - size (sqm)
  - furnished status
  - listing URL

## Purpose

This project was created to:

- Practice Python and data analysis
- Build a practical tool using real-world data
- Improve skills in data processing, visualization, and UI design

## How to Run

1. Install dependencies:

```bash
pip install pandas streamlit
```

2. Run the app:

```bash
streamlit run app/streamlit_app_real.py
```

## Future Improvements

- Increase dataset size (100+ listings)
- Add map-based visualization
- Automate data collection (scraping)
- Add user preference weighting for recommendations
- Improve UI desighn

## Demo

- App URL: https://vilnius-rent-analyzer-real.streamlit.app