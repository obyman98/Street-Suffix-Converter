import pandas as pd

# Names Initializations
filename = 'addresses.csv'
column = 'Addresses'
newcolumn = 'Converted Addresses'

# Load the street type abbreviations from the CSV file
abbreviations_df = pd.read_csv("australian_street_types.csv")
abbreviation_dict = pd.Series(abbreviations_df.Abbreviation.values, index=abbreviations_df["Street Type"]).to_dict()
full_name_dict = pd.Series(abbreviations_df["Street Type"].values, index=abbreviations_df.Abbreviation).to_dict()

# Function to replace street types with abbreviations or vice versa
def replace_street_types(name, mapping_dict):
    words = name.split()
    # Replace the last word in the address if it matches the mapping dictionary
    if words[-1].upper() in mapping_dict:
        words[-1] = mapping_dict[words[-1].upper()]
    return " ".join(words)

# Read the original CSV file
df = pd.read_csv(filename)

# Select conversion direction
conversion_type = input("Enter '1' to convert full street names to abbreviations or '2' to convert abbreviations to full street names: ")

# Self explainatory at this point(Read the above output for further clarification)
if conversion_type == '1':
    df[newcolumn] = df[column].apply(replace_street_types, mapping_dict=abbreviation_dict)
elif conversion_type == '2':
    df[newcolumn] = df[column].apply(replace_street_types, mapping_dict=full_name_dict)
else:
    print("Invalid input. Please enter '1' or '2'.")

# Save the updated DataFrame to the same CSV file, adding the new column
df.to_csv(filename, index=False)

print("Street types have been successfully converted and added as a new column to the same file.")
