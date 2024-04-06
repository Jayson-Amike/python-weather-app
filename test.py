import numpy as np
from getLoc import table_data


# Get the first column
first_column = [row[0] for row in table_data]

# Store the remaining data
remaining_data = [[row[1], row[2]] for row in table_data]

# Create a dictionary to associate the first column with the remaining data
data_dict = {first_column[i]: remaining_data[i] for i in range(len(first_column))}

# Example usage: If you have a value from the first column, you can find its corresponding data
search_value = "Yorkton, SK, Canada"
corresponding_data = data_dict.get(search_value)

print("Data corresponding to", search_value, ":", corresponding_data)  # Output: [5, 6]