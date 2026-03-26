# Vilnius Rent Analyzer

Vilnius Rent Analyzer is a simple web app for comparing student housing options in Vilnius.

This app allows users to filter rental listings by price, distance to VILNIUS TECH, district, room type, and furnished status. It also shows summary statistics and a bar chart of average rent by district.

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

## Future Improvements

- Replace sample data with real housing listing data
- Add map-based visualization
- Add PostgreSQL support
- Add FastAPI backend for future expansion
- Improve table formatting and result detail view