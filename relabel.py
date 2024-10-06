import os

def change_labels(folder_path):
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):  # Assuming YOLO label files are .txt
            file_path = os.path.join(folder_path, filename)
            
            # Read the content of the file
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            # Modify the lines
            modified_lines = []
            for line in lines:
                parts = line.strip().split()
                if parts:
                    # Change the class index from 0 to 1
                    parts[0] = '1' if parts[0] == '0' else parts[0]
                    modified_lines.append(' '.join(parts) + '\n')
            
            # Write the modified content back to the file
            with open(file_path, 'w') as file:
                file.writelines(modified_lines)
            
            print(f"Processed: {filename}")

# Usage
folder_path = './valid/old_labels/'  # Replace with your actual folder path
change_labels(folder_path)

print("Label modification completed.")