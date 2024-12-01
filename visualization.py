import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
file_path = "../data/crime_data_cleaned.csv"
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("Cleaned Data Preview:")
print(data.head())

# Visualization 1: Line plot of crime trends over years
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='year', y='total_cases', hue='region')
plt.title("Crime Trends by Region")
plt.xlabel("Year")
plt.ylabel("Total Cases")
plt.legend(title="Region")
plt.savefig("../visuals/crime_trends_by_region.png")
plt.show()

# Visualization 2: Bar plot of total crimes by region
region_crimes = data.groupby('region')['total_cases'].sum().reset_index()
plt.figure(figsize=(8, 6))
sns.barplot(data=region_crimes, x='region', y='total_cases')
plt.title("Total Crimes by Region")
plt.xlabel("Region")
plt.ylabel("Total Cases")
plt.xticks(rotation=45)
plt.savefig("../visuals/crime_total_by_region.png")
plt.show()
