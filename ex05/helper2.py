import csv

def get_highest_income(csv_file):
    highest_income = float('-inf')  # Start with a very low value

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Access the 'income' column and convert it to float
            income = float(row['income'])

            # Update highest_income if the current income is higher
            if income > highest_income:
                highest_income = income

    return highest_income

# Specify the path to your CSV file
csv_file_path = 'bank-data.csv'

try:
    # Call the function to get the highest income
    highest_income = get_highest_income(csv_file_path)

    # Print the highest income found
    print(f"The highest income is: ${highest_income:.2f}")

except FileNotFoundError:
    print(f"Error: CSV file not found at '{csv_file_path}'")
except ValueError:
    print("Error: Unable to convert 'income' to a valid number")
except Exception as e:
    print(f"An error occurred: {e}")
