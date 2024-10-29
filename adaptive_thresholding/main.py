import argparse
import os
import pandas as pd
from tqdm import tqdm
from adaptive_thresholding.utils import load_data, save_data
from adaptive_thresholding.thresholds.adaptive import adaptive_thresholding

def main():
    parser = argparse.ArgumentParser(description="Adaptive Thresholding Tool")
    parser.add_argument("input_folder", type=str, help="Folder containing input CSV files")
    parser.add_argument("output_folder", type=str, help="Folder to store output CSV files")
    parser.add_argument("--marker_columns", nargs="+", required=True, help="List of marker columns for thresholding.")
    args = parser.parse_args()

    # Ensure output directory exists
    os.makedirs(args.output_folder, exist_ok=True)

    # Process each file in the input folder
    for file in tqdm(os.listdir(args.input_folder)):
        if file.endswith(('.csv', '.txt')):
            # Load data
            file_path = os.path.join(args.input_folder, file)
            df = load_data(file_path)

            # Apply adaptive thresholding to specified marker columns
            processed_df = adaptive_thresholding(df, args.marker_columns, args.output_folder, file)

            # Save processed data to output folder
            save_data(processed_df, os.path.join(args.output_folder, file))

if __name__ == "__main__":
    main()
