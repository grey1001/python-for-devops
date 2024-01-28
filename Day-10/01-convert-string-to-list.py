import os
folder_paths = input("Please enter folder paths with spaces: ").split() # split coverts strings to lists
for folder in folder_paths:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name")
        break # this continues on to the next correct input. Use break instead to exit the code
    print(f"Listing files from the folder {folder}")
    for file in files:
        print(file)