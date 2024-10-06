import os
import shutil
import random

def adjust_split(base_path, train_folder='train', test_folder='test', target_test_ratio=0.2):
    # Get the total number of images
    train_images = os.listdir(os.path.join(base_path, train_folder, 'images'))
    test_images = os.listdir(os.path.join(base_path, test_folder, 'images'))
    total_images = len(train_images) + len(test_images)
    
    # Calculate the target number of test images
    target_test_count = int(total_images * target_test_ratio)
    
    # Determine how many images to move
    if len(test_images) < target_test_count:
        # Move images from train to test
        num_to_move = target_test_count - len(test_images)
        source_folder = train_folder
        dest_folder = test_folder
        images_to_move = random.sample(train_images, num_to_move)
    else:
        # Move images from test to train
        num_to_move = len(test_images) - target_test_count
        source_folder = test_folder
        dest_folder = train_folder
        images_to_move = random.sample(test_images, num_to_move)
    
    # Move the files
    for img in images_to_move:
        # Move image
        shutil.move(
            os.path.join(base_path, source_folder, 'images', img),
            os.path.join(base_path, dest_folder, 'images', img)
        )
        
        # Move corresponding label
        label = img.rsplit('.', 1)[0] + '.txt'  # Assuming labels are .txt files
        shutil.move(
            os.path.join(base_path, source_folder, 'labels', label),
            os.path.join(base_path, dest_folder, 'labels', label)
        )
    
    print(f"Moved {num_to_move} images and labels from {source_folder} to {dest_folder}")
    print(f"New split: Train: {len(os.listdir(os.path.join(base_path, train_folder, 'images')))}, "
          f"Test: {len(os.listdir(os.path.join(base_path, test_folder, 'images')))}")

# Usage
base_path = './'  # Replace with your actual path
adjust_split(base_path)