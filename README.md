# 🌦 Weather Data Analysis

## 📌 Project Overview

This project performs data cleaning and analysis on a weather dataset.
The workflow includes:

1. Loading raw weather data (with missing & invalid values)

2. Cleaning and preprocessing the dataset

3. Generating visualizations

4. Producing a statistical summary

5. Exporting all results as files


Everything is automated using the script pp.py.


---

# 📁 Files in This Project

File Name	Description

weather.csv	Raw uncleaned weather data (contains missing & invalid values).

pp.py	Python script that cleans data, generates plots, and creates summary.

cleaned_weather_data.csv	Output cleaned dataset.

temp_trend.png	Line plot showing temperature changes over time.

humidity_vs_temp.png	Scatter plot comparing humidity and temperature.

monthly_rain.png	Bar chart showing daily rainfall.

summary.txt	File containing average temperature, humidity, and total rainfall.



---

# 🧹 Data Cleaning Steps

The pp.py script performs the following operations:

1. Load raw CSV file


2. Convert Date column to datetime, invalid dates become NaT


3. Drop rows with missing/invalid dates


4. Fill missing values with column means:

Temperature → mean = 28.2

Rainfall → mean = 4.08

Humidity → mean = 63.4



5. Save the cleaned dataset as cleaned_weather_data.csv




---

# 📊 Generated Visualizations

1. Temperature Trend (temp_trend.png)

Shows temperature changes over the cleaned date range.

2. Humidity vs Temperature (humidity_vs_temp.png)

Scatter plot showing how humidity varies with temperature.

3. Daily Rainfall (monthly_rain.png)

Bar chart with rainfall for each valid day in the dataset.


---

# 📝 Summary File

## summary.txt contains:

Average Temperature: 28.20

Average Humidity: 63.40

Total Rainfall: 28.56


---

# ▶ How to Run pp.py

## Requirements

Install required libraries:

pip install pandas matplotlib

## Run the Script

Make sure weather.csv exists in the same folder.
Then run:

python pp.py

This will automatically generate:

1. cleaned_weather_data.csv

2. summary.txt

3. temp_trend.png

4. humidity_vs_temp.png

5. monthly_rain.png



---

# ✅ Output Folder Structure

📁 Project
│── weather.csv
│── pp.py
│── cleaned_weather_data.csv
│── summary.txt
│── temp_trend.png
│── humidity_vs_temp.png
│── monthly_rain.png
│── README.md  (this file)


---


# Author 

Ishant Singh

2501410067

BTech CSE (Cyber Security)


---
