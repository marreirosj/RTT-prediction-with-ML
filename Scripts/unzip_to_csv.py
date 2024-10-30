import shutil
import os
import zipfile
import pandas as pd
from joblib import Parallel, delayed
import sys

def unzip_file(zip_file_path, output_folder):
  
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(output_folder)
            print(f"Unzipped {zip_file_path} to {output_folder}")
    except zipfile.BadZipFile:
        print(f"Error: {zip_file_path} is not a zip file or it is corrupted.")
    except Exception as e:
        print(f"Error extracting {zip_file_path}: {e}")

def process_zip_files(folder_path, output_folder):
   
    zip_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith('.zip')]
    
    if not zip_files:
        print("No zip files found in the specified folder.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  

    Parallel(n_jobs=-1)(delayed(unzip_file)(zip_file, output_folder) for zip_file in zip_files)

def merge_txt_files_in_chunks(input_folder, output_file, chunk_size=100000):
    
    txt_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.lower().endswith('.txt')]
    
    if not txt_files:
        print("No .txt files found in the output folder.")
        return
    
    csv_created = False
    
    for txt_file in txt_files:
        print(f"Processing {txt_file}...")

        for chunk in pd.read_csv(txt_file, delimiter='|', encoding='utf-8', chunksize=chunk_size):
            
            if not csv_created:
                chunk.to_csv(output_file, index=False, mode='w')  
                csv_created = True
            else:
                chunk.to_csv(output_file, index=False, mode='a', header=False)  

    print(f"All .txt files have been merged into {output_file}.")

def main(zip_folder_path, output_folder, merged_csv_file):
    if not os.path.isdir(zip_folder_path):
        print(f"Error: The folder path '{zip_folder_path}' does not exist.")
        return

    print(f"Using output folder: {output_folder}")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    process_zip_files(zip_folder_path, output_folder)

    merge_txt_files_in_chunks(output_folder, merged_csv_file)

    print("Process completed.")
    
    cache_path = "./Scripts/__pycache__"
    if os.path.exists(cache_path):
        shutil.rmtree(cache_path)
        print(f"Deleted cache folder: {cache_path}")

if __name__ == "__main__":    
    if len(sys.argv) != 4:
        print("Usage: python script.py <zip_folder_path> <output_folder> <merged_csv_file>")
        sys.exit(1)
    
    zip_folder_path = sys.argv[1]
    output_folder = sys.argv[2]
    merged_csv_file = sys.argv[3]

    main(zip_folder_path, output_folder, merged_csv_file)
