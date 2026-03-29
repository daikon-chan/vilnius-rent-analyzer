# Vilnius Rent Analyzer

Vilnius Rent Analyzer is a simple web app designed to help students compare housing options in Vilnius, especially those studying at VILNIUS TECH.

This project was built as a prototype to explore how data analysis can support decision-making when searching for housing.

## Features

- Filter listings by:
  - maximum rent
  - maximum distance to VILNIUS TECH
  - district
  - room type
  - furnished / unfurnished
- Sort results by:
  - lowest rent
  - highest rent
  - nearest distance
  - largest size
- View summary metrics:
  - number of results
  - average rent
  - minimum rent
  - maximum rent
- View a bar chart of average rent by district
- Download filtered results as CSV

## Tech Stack

- Python
- pandas
- Streamlit

## Current Data

The current version uses a sample CSV dataset for prototyping and UI development.

## Purpose

This project is part of my learning journey in Python and data analysis, focusing on building practical tools using real-world use cases.

## How to Run

1. Install dependencies:

```bash
pip install pandas streamlit
```

2. Run the app:

```bash
streamlit run app/streamlit_app.py
```

## Future Improvements

- Replace sample data with real housing listing data
- Add map-based visualization
- Add PostgreSQL support
- Add FastAPI backend for future expansion
- Improve table formatting and result detail view

## Demo

- App URL: https://vilnius-rent-analyzer.streamlit.app