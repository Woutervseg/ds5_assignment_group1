def read_csv(file_path):
    """
    Reads a CSV file and returns a list of records as dictionaries.
    """
    records = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            records.append(row)
    return records

def calculate_average(records):
    """
    Calculates the average grade from a list of records.
    """
    if not records:
        return None  # Return None if there are no records

    total = sum(float(record['Grade']) for record in records)
    average = total / len(records)
    return average

def print_student_report(records):
    """
    Prints a student report for records with grades >= 80.
    """
    print("Student Report")
    print("--------------")
    for record in records:
        print(f"Name: {record['Name']}")
        print(f"Grade: {record['Grade']}")
        print("--------------------")

# Get the CSV file path from the user
file_path = input("Enter the path to the CSV file: ")

# Read the CSV file and store records
records = read_csv(file_path)

# Calculate the average grade
average = calculate_average(records)

# Print the average grade if it's available
if average is not None:
    print(f"Average Grade: {average}\n")

# Filter and print the student report for grades >= 80
filtered_records = [record for record in records if float(record['Grade']) >= 80.0]
print_student_report(filtered_records)
