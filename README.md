# Bike Sharing Analysis Dashboard

This dashboard provides an analysis of bike sharing usage in Washington D.C. based on the Bike Sharing Dataset. It includes visualizations of user types, seasonal trends, weekday vs. weekend usage, and hourly usage patterns.

## Prerequisites

Before running the dashboard, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone this repository or download the source code.

```
git clone https://github.com/raflyranggha/Bike-Sharing-Analysis.git
cd Bike-Sharing-Analysis
```

2. Install the required packages:

```
pip install -r requirements.txt
```

## Data Preparation

Ensure you have the following CSV files in the same directory as the script:

- `day_cleaned.csv`
- `hour_cleaned.csv`

These files should contain the cleaned bike sharing data for daily and hourly records respectively.

## Running the Dashboard

To run the dashboard, use the following command:

```
streamlit run app.py
```

This will start a local Streamlit server and open the dashboard in your default web browser. If it doesn't open automatically, you can access it by navigating to the URL shown in the terminal (usually `http://localhost:8501`).

## Using the Dashboard

1. The dashboard will load with default settings showing data for all available dates and years.

2. Use the sidebar to apply filters:
   - Check the "Apply Date and Year Filter" box to enable filtering.
   - Select a date range using the date picker.
   - Choose specific years using the multi-select dropdown.

3. Explore the various visualizations:
   - Total Registered and Casual Users
   - Bike Usage Trends by Year
   - Bike Usage Patterns by Season
   - Weekday vs. Weekend Usage
   - Hourly Usage Distribution

4. Interact with the charts by hovering over data points for more information.
