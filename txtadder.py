import os

def add_txt_extension_to_files():
    
    current_directory = os.getcwd()
    print(f"Checking files in: {current_directory}")

    for filename in os.listdir(current_directory):
        file_path = os.path.join(current_directory, filename)
        if os.path.isfile(file_path):
            if not filename.lower().endswith('.py'):
                if not filename.lower().endswith('.txt'):
                    new_filename = filename + '.txt'
                    new_file_path = os.path.join(current_directory, new_filename)
                    try:
                        os.rename(file_path, new_file_path)
                        print(f"Renamed '{filename}' to '{new_filename}'")
                    except OSError as e:
                        print(f"Error renaming '{filename}': {e}")
                else:
                    print(f"Skipping '{filename}', already has .txt extension.")
            else:
                print(f"Skipping '{filename}', it's a Python script (.py).")
        else:
            print(f"Skipping '{filename}', it's a directory.")

if __name__ == "__main__":
    add_txt_extension_to_files()
    print("\nProcess complete.")

