#Run it only once -> Each time you run it datasets will be replaces by new

#this is another method so instead of you guys downloading it i have the folder here and this code splits it into train,test,validation datasets

import os
import random
import shutil

# Define paths
source_data_dir = 'MalariaDataset/cell_images'
output_dir = 'MalariaDataset/SplitData'

# Create output directories
train_dir = os.path.join(output_dir, 'train')
validation_dir = os.path.join(output_dir, 'validation')
test_dir = os.path.join(output_dir, 'test')

os.makedirs(train_dir, exist_ok=True)
os.makedirs(validation_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Define the ratio for splitting the data
train_ratio = 0.90  # 90% for training
validation_ratio = 0.05  # 5% for validation
test_ratio = 0.05  # 5% for testing

# Iterate through each class folder in the source data directory
for class_folder in os.listdir(source_data_dir):
    class_path = os.path.join(source_data_dir, class_folder)
    
    # List all the image files in the class folder
    files = os.listdir(class_path)
    num_files = len(files)
    
    # Shuffle the files randomly
    random.shuffle(files)
    
    # Calculate split indices
    train_split = int(train_ratio * num_files)
    validation_split = int((train_ratio + validation_ratio) * num_files)
    
    # Split the files into train, validation, and test sets
    train_files = files[:train_split]
    validation_files = files[train_split:validation_split]
    test_files = files[validation_split:]
    
    # Move files to their respective directories
    for file in train_files:
        src_file = os.path.join(class_path, file)
        dst_file = os.path.join(train_dir, class_folder, file)
        os.makedirs(os.path.dirname(dst_file), exist_ok=True)
        shutil.copy(src_file, dst_file)
    
    for file in validation_files:
        src_file = os.path.join(class_path, file)
        dst_file = os.path.join(validation_dir, class_folder, file)
        os.makedirs(os.path.dirname(dst_file), exist_ok=True)
        shutil.copy(src_file, dst_file)
    
    for file in test_files:
        src_file = os.path.join(class_path, file)
        dst_file = os.path.join(test_dir, class_folder, file)
        os.makedirs(os.path.dirname(dst_file), exist_ok=True)
        shutil.copy(src_file, dst_file)
