import pandas as pd
import os
import sys

def split_by_shipvoyage(input_file: str, output_folder: str) -> None:
    """
    Split the cleaned dataset into separate CSV files based on unique ShipVoyage values.

    Parameters:
        input_file (str): Path to the cleaned CSV file.
        output_folder (str): Folder to save the ShipVoyage-specific CSV files.
    """
    # Load the cleaned dataset
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading the data: {e}")
        sys.exit(1)

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Get the unique ShipVoyage values
    unique_voyages = df['ShipVoyage'].unique()

    # Iterate through each unique ShipVoyage and save it as a separate CSV file
    for voyage in unique_voyages:
        # Sanitize the ShipVoyage value for file naming
        sanitized_voyage = str(voyage).replace(":", "_").replace("/", "_")
        
        # Filter the data for the current ShipVoyage
        voyage_data = df[df['ShipVoyage'] == voyage]
        
        # Define the output file name (e.g., ShipVoyage_1234.csv)
        output_file = os.path.join(output_folder, f'ShipVoyage_{sanitized_voyage}.csv')
        
        # Save the data for the current ShipVoyage to a CSV file
        voyage_data.to_csv(output_file, index=False)
        print(f"Saved {output_file}")

      
# Modify main to accept arguments directly
def main(input_file: str = None, output_folder: str = None):
    """
    Main function to execute the splitting of the dataset by ShipVoyage.
    If no arguments are provided, it will attempt to use command-line arguments.
    
    Parameters:
        input_file (str): Path to the cleaned CSV file.
        output_folder (str): Folder to save the ShipVoyage-specific CSV files.
    """
    if input_file is None or output_folder is None:
        if len(sys.argv) != 3:
            print("Usage: python single_csv.py <input_file> <output_folder>")
            sys.exit(1)
        # Get the input arguments from the command line
        input_file = sys.argv[1]
        output_folder = sys.argv[2]

    # Call the function to split by ShipVoyage and get the voyage count
    voyage_count = split_by_shipvoyage(input_file, output_folder)
    
    # Display the number of voyages split
    display(f"Total voyages split into separate CSV files: {voyage_count}")

# If this script is run from the command line
if __name__ == "__main__":
    main()

