# 🛣️ Street Type Converter

Welcome to the **Street Type Converter** repo! 🎉 This project is all about making your life easier when dealing with street names in Australia. Whether you need to convert full street names to their abbreviations (like "Street" to "St") or turn those abbreviations back into full names, this script has got you covered.

## What’s Inside? 📦

- **Python Script**: A Python script that does all the heavy lifting. It reads a CSV file, converts street types in the `Name` column either to their abbreviations or full names, and adds a new column with the results.
- **Street Types CSV**: A handy CSV file (`australian_street_types.csv`) listing all the street types and their abbreviations used in Australia.
- **Sample File**: A sample CSV file (`large_file.csv`) with 6000 rows (okay, maybe not literally 6000, but you get the idea 😉) to show you how the conversion works in real-life scenarios.

## How It Works 🔧

1. **Choose Your Conversion**: Run the script and choose whether you want to convert full street names to abbreviations or the other way around.
2. **Magic Happens**: The script reads your CSV, does the conversion, and adds a new column called `Converted_Name` with the updated values.
3. **Done!**: Your CSV now has a new column with the converted street names. The original `Name` column stays untouched, so no worries about messing anything up.

## Why This Exists? 🤔

Ever had to standardize addresses in a dataset? It’s a pain, right? This script automates the tedious task of converting street names, making sure everything is consistent and in line with Aussie standards. Whether you're a data scientist, developer, or just someone who deals with large address datasets, this tool will save you a ton of time.

## How to Use It 🚀

1. Clone the repo: git clone https://github.com/yourusername/street-type-converter.git cd street-type-converter
2. Install the required packages (if you haven’t already): pip install pandas
3. Run the script: python street_type_conversion.py
4. Follow the prompt to choose your conversion type and let the script do the rest!

## Sample File 🗂️

Check out the `addresses.csv` in this repo. It's a sample dataset showing how the conversion works. You can play around with it or replace it with your own dataset.

## Contribute 🤝

Found a bug or want to add a feature? Feel free to fork the repo and submit a pull request. Let’s make this tool even better together!

## License 📄

This project is open-source, and you can use it however you like. Just be sure to give credit where it's due! 😄

