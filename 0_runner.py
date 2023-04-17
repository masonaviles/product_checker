import os
import time

# Get the path of the directory containing this script
script_dir_path = os.path.dirname(os.path.abspath(__file__))

# Set the relative path of the directory containing the Python files
python_dir_rel_path = "python_files"

# Get the absolute path of the directory containing the Python files
python_dir_path = os.path.join(script_dir_path, python_dir_rel_path)

# Run the files in the directory once an hour
while True:
    for filename in os.listdir(python_dir_path):
        if filename.endswith(".py"):
            os.system(f"python {os.path.join(python_dir_path, filename)}")
    time.sleep(3600)  # Wait for an hour before running the files again