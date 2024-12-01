import pandas as pd
import os

# File paths
input_file_path = "../data/crime_data_raw.csv"  # Raw data file
output_file_path = "../data/crime_data_cleaned.csv"  # Cleaned data file

# Check if the raw data file exists
if os.path.exists(input_file_path):
    # Load the raw dataset
    data = pd.read_csv(input_file_path)

    # Display the first few rows of the dataset
    print("Raw Data Preview:")
    print(data.head())

    # Data Cleaning Steps (Example)
    # Remove rows with missing values
    data = data.dropna()

    # Standardize column names
    data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')

    # Save the cleaned data to a new file
    data.to_csv(output_file_path, index=False)
    print(f"Cleaned data saved to {output_file_path}")
else:
    print(f"Error: The file '{input_file_path}' does not exist. Please check the file path.")
