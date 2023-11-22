# Open the file for reading
try:
    with open('2023-11-22T02_18_49_39977_2023-11-22T02_18_49_39977.overall_export_metadata', 'r') as file:
        # Read the contents of the file
        data = file.read()
        # Do something with the data
        print(data)
except FileNotFoundError:
    print("The file '.overall_export_metadata' does not exist.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
