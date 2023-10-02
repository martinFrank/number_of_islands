import csv

def read_csv(path):
    # Replace 'your_csv_file.csv' with the actual path to your CSV file
    #csv_file_path = 'your_csv_file.csv'
    #csv_file_path = 'C:\\Users\\m.frank\\IdeaProjects\\privat\\pyIslands\\src\\resources\\island_01.csv'
    csv_file_path = path

    # Initialize an empty list to store the data
    data = []

    # Open the CSV file and read its contents
    with open(path, 'r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        
        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Append each row as a list to the 'data' list
            data.append(row)
            print(f"adding {row}")

    # Now, 'data' contains a list of lists, where each inner list represents a row in the CSV file

    return data