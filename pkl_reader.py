import os
import pickle
import numpy as np

# Get the current directory
current_directory = os.getcwd()

# Traverse all files in the current directory
for root, dirs, files in os.walk(current_directory):
    for file in files:
        if file.endswith('.pkl'):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'rb') as pkl_file:
                    data = pickle.load(pkl_file)
                    print(f"Data from {file_path}:")
                    print("---------------------- stats ----------------------")
                    for key in data['stats']:
                        print(f"{key}: {data['stats'][key]}")
            except Exception as e:
                print(f"Failed to read {file_path}: {e}")