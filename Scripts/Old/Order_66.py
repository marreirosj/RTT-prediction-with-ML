import os
import zipfile
import pandas as pd
import multiprocessing

def unzip_file(zip_file_path, output_folder):
    """
    Unzips a single file to the specified output folder.
    """
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(output_folder)
            print(f"Unzipped {zip_file_path} to {output_folder}")
    except zipfile.BadZipFile:
        print(f"Error: {zip_file_path} is not a zip file or it is corrupted.")
    except Exception as e:
        print(f"Error extracting {zip_file_path}: {e}")

def process_zip_files(zip_files, output_folder):
    """
    Process zip files using multiprocessing, based on the number of CPU cores.
    """
    if not zip_files:
        print("No zip files found in the specified folder.")
        return

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Utilize the number of CPU cores to determine the processes count
    num_cores = multiprocessing.cpu_count()
    with multiprocessing.Pool(processes=num_cores) as pool:
        pool.starmap(unzip_file, [(zip_file, output_folder) for zip_file in zip_files])

def process_txt_file(file_path):
    """
    Reads a single .txt file and returns it as a pandas DataFrame.
    """
    try:
        return pd.read_csv(file_path, delimiter='|', encoding='utf-8')
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return pd.DataFrame()

def merge_txt_files(input_folder, output_file):
    """
    Merges all .txt files in the input folder into a single CSV file.
    Processes files in parallel using multiprocessing.
    """
    txt_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.lower().endswith('.txt')]

    if not txt_files:
        print("No .txt files found in the folder.")
        return

    num_cores = multiprocessing.cpu_count()
    with multiprocessing.Pool(processes=num_cores) as pool:
        dataframes = pool.map(process_txt_file, txt_files)

    # Concatenate all DataFrames and write to CSV
    all_data = pd.concat(dataframes, ignore_index=True)
    all_data.to_csv(output_file, index=False)
    print(f"Merged .txt files into {output_file}")

def main(zip_folder_path, merged_csv_file, unzip_folder):
    if not os.path.isdir(zip_folder_path):
        print(f"Error: The folder path '{zip_folder_path}' does not exist.")
        return

    # Set the output folder for unzipped files
    output_folder = unzip_folder

    # Get all zip files from the folder
    zip_files = [os.path.join(zip_folder_path, f) for f in os.listdir(zip_folder_path) if f.lower().endswith('.zip')]

    # Unzip files to the specified folder
    process_zip_files(zip_files, output_folder)

    # Merge .txt files in the unzipped folder into a single CSV file
    merge_txt_files(output_folder, merged_csv_file)

if __name__ == "__main__":
    zip_folder_path = "./zip"
    merged_csv_file = "merged_output.csv"
    unzip_folder = "./unzipped"  # Specify the folder where the files will be unzipped

    main(zip_folder_path, merged_csv_file, unzip_folder)
