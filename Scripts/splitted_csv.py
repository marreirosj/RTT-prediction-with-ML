import pandas as pd
import os
import sys

def split_by_shipvoyage(input_file: str, output_folder: str) -> None:
    
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading the data: {e}")
        sys.exit(1)
    
    os.makedirs(output_folder, exist_ok=True)
    
    unique_voyages = df['ShipVoyage'].unique()
    
    for voyage in unique_voyages:        
        sanitized_voyage = str(voyage).replace(":", "_").replace("/", "_")
        
        voyage_data = df[df['ShipVoyage'] == voyage]
        
        output_file = os.path.join(output_folder, f'ShipVoyage_{sanitized_voyage}.csv')
        
        voyage_data.to_csv(output_file, index=False)
        print(f"Saved {output_file}")

 
def main(input_file: str = None, output_folder: str = None):
    
    if input_file is None or output_folder is None:
        if len(sys.argv) != 3:
            print("Usage: python single_csv.py <input_file> <output_folder>")
            sys.exit(1)
        input_file = sys.argv[1]
        output_folder = sys.argv[2]

    voyage_count = split_by_shipvoyage(input_file, output_folder)
    
    display(f"Total voyages split into separate CSV files: {voyage_count}")

if __name__ == "__main__":
    main()

