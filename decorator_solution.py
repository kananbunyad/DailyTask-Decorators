import os
import sys
import datetime

# Decorator to log file operations
def log_file_operation(func):
    def wrapper(*args, **kwargs):
        operation_type = func.__name__.replace("_file", "").capitalize()
        file_path = args[0] if args else kwargs.get("file_path", "")
        print(f"Operation: {operation_type}")
        print(f"File Path: {file_path}")
        print(f"Date and Time: {datetime.datetime.now()}")
        print(f"Process ID: {os.getpid()}\n")
        result = func(*args, **kwargs)
        return result
    return wrapper

# Function to create a new file
@log_file_operation
def create_file(directory_path, file_name):
    try:
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, 'w') as file:
            file.write(f"Operation: Create\n")
            file.write(f"File Path: {file_path}\n")
            file.write(f"Date and Time: {datetime.datetime.now()}\n")
            file.write(f"Process ID: {os.getpid()}\n\n")
        print("File created successfully")
    except Exception as e:
        print(f"Error occurred while creating file: {str(e)}")

# Function to delete a file

def delete_file(file_path):
    try:
        os.remove(file_path)
        print("File deleted successfully")
    except FileNotFoundError:
        print("File not found, please check the file path")
    except PermissionError:
        print("Permission denied. Unable to delete the file.")
    except Exception as e:
        print(f"Error occurred while deleting file: {str(e)}")

# Function to rename a file
@log_file_operation
def rename_file(old_file_path, new_file_path):
    try:
        os.rename(old_file_path, new_file_path)
        with open(new_file_path, 'a') as file:
            file.write(f"Operation: Rename\n")
            file.write(f"File Path: {file_path}\n")
            file.write(f"Date and Time: {datetime.datetime.now()}\n")
            file.write(f"Process ID: {os.getpid()}\n\n")
        print("File renamed successfully")
    except FileNotFoundError:
        print("File not found, please check the file path")
    except PermissionError:
        print("Permission denied. Unable to rename the file.")
    except Exception as e:
        print(f"Error occurred while renaming file: {str(e)}")

directory_path = os.getcwd()

if len(sys.argv) == 3 and sys.argv[1] == 'create':
    file_name = sys.argv[2]
    create_file(directory_path, file_name)
elif len(sys.argv) == 4 and sys.argv[1] == 'rename':
    old_file_name = sys.argv[2]
    new_file_name = sys.argv[3]
    file_path = os.path.join(directory_path, old_file_name)
    renamed_file_path = os.path.join(directory_path, new_file_name)
    rename_file(file_path, renamed_file_path)
elif len(sys.argv) == 3 and sys.argv[1] == 'delete':
    file_name = sys.argv[2]
    file_path = os.path.join(directory_path, file_name)
    delete_file(file_path)
else:
    print("Invalid command. Usage:")
    print("To create a file: python task.py create [file_name]")
    print("To delete a file: python task.py delete [file_name]")
    print("To rename a file: python task.py rename [old_file_name] [new_file_name]")
