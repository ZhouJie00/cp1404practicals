"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    for line in data:
        print(f"{line[0]} is taught by {line[1]} and has {line[1]} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    formatted_data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        formatted_data.append(parts)
    input_file.close()
    return formatted_data


main()