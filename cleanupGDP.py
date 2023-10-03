# Define the input and output file paths
input_file = 'us_gdp_claude.csv'
output_file = 'us_gdp_claude_cleaned.csv'

# Open the input file for reading and the output file for writing
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    # Iterate through each line in the input file
    for line in infile:
        # Split the line by comma
        parts = line.split(',')

        # If there are more than two parts (two commas), join the second and subsequent parts
        if len(parts) > 2:
            cleaned_line = parts[0] + ',' + ''.join(parts[1:])
        else:
            cleaned_line = line  # No changes needed

        # Write the cleaned line to the output file
        outfile.write(cleaned_line)

# Print a message indicating the cleanup is complete
print("Cleanup complete. Cleaned data saved to", output_file)
