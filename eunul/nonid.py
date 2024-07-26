import os

def is_folder_empty(folder_path):
    """
    Checks if the specified folder is empty.
    
    :param folder_path: Path to the folder to check.
    :return: True if the folder is empty, False otherwise.
    """
    try:
        items_in_folder = os.listdir(folder_path)
        return not items_in_folder
    except FileNotFoundError:
        print(f"The folder '{folder_path}' does not exist.")
        return False
    except PermissionError:
        print(f"Permission denied to access the folder '{folder_path}'.")
        return False

# Example usage:
folder_path = "/path/to/folder"
if is_folder_empty(folder_path):
    print("The folder is empty.")
else:
    print("The folder is not empty.")
