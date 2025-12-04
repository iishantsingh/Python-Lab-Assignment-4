import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Load Weather Data
# -------------------------------
df = pd.read_csv("weather.csv")

# -------------------------------
# Clean Data
# -------------------------------

# Convert Date column to datetime and convert invalid dates to NaT
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Drop rows where Date is missing or invalid
df = df.dropna(subset=["Date"])

# Fill missing numeric values with column means
df["Temperature"] = df["Temperature"].fillna(df["Temperature"].mean())
df["Rainfall"] = df["Rainfall"].fillna(df["Rainfall"].mean())
df["Humidity"] = df["Humidity"].fillna(df["Humidity"].mean())

# Save cleaned CSV
df.to_csv("cleaned_weather_data.csv", index=False)

# -------------------------------
# Temperature Trend Plot
# -------------------------------
plt.figure()
plt.plot(df["Date"], df["Temperature"])
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Temperature Trend")
plt.savefig("temp_trend.png")
plt.close()

# -------------------------------
# Humidity vs Temperature Plot
# -------------------------------
plt.figure()
plt.scatter(df["Temperature"], df["Humidity"])
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.title("Humidity vs Temperature")
plt.savefig("humidity_vs_temp.png")
plt.close()

# -------------------------------
# Monthly Rainfall Plot
# -------------------------------
plt.figure()
plt.bar(df["Date"].dt.day, df["Rainfall"])
plt.xlabel("Day of Month")
plt.ylabel("Rainfall")
plt.title("Daily Rainfall")
plt.savefig("monthly_rain.png")
plt.close()

# -------------------------------
# Summary File
# -------------------------------
summary = (
    f"Average Temperature: {df['Temperature'].mean():.2f}\n"
    f"Average Humidity: {df['Humidity'].mean():.2f}\n"
    f"Total Rainfall: {df['Rainfall'].sum():.2f}\n"
)

with open("summary.txt", "w") as file:
    file.write(summary)

print("All files generated successfully!")