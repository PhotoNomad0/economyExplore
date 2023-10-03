import pandas as pd

# Define the file paths for the two CSV files and the output CSV file
file1 = "us_gdp_claude_cleaned.csv"
file2 = "us_rates_claude.csv"
output_file = "ratesVsGdp.csv"

# Read the CSV files into pandas DataFrames
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Merge the DataFrames using the "Year" column as the common index
merged_df = pd.merge(df1, df2, on="Year")

# Save the merged DataFrame to a new CSV file
merged_df.to_csv(output_file, index=False)

print("Merge complete. Merged data saved to", output_file)
