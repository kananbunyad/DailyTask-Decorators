# Python  :snake:

We require you to solve the following tasks. Remember to read the requirements first.

#### Topics you need to know and use to solve tasks

* Working with files
* Exception handling
* Decorators in Python

**Final Notes**: *Remember to solve and send assignments on time* :hourglass_flowing_sand:

# Assignments' list 

## Assignment 1  :star:  :star:  :star:  :star:  :star2:

### Description 

In this assignment, you are tasked with creating a Python script that performs file operations such as creating, deleting, and renaming files. The script also includes a decorator that logs the details of each file operation.


### Create a File

To create a file, use the following command:
```
python task.py create [file_name]
```
Replace `[file_name]` with the desired name for the new file.

### Delete a File

To delete a file, use the following command:
```
python task.py delete [file_name]
```

Replace `[file_name]` with the name of the file you want to delete.

### Rename a File

To rename a file, use the following command:
```
python task.py rename [old_file_name] [new_file_name]
```

Replace `[old_file_name]` with the current name of the file and `[new_file_name]` with the desired new name.

Note: The script assumes that the files are located in the same directory as the script itself.



## Command Line Arguments

The script accepts command line arguments to determine the operation to perform and the file names. The following arguments are supported:

- `create [file_name]`: Creates a new file with the specified name.
- `delete [file_name]`: Deletes the file with the specified name.
- `rename [old_file_name] [new_file_name]`: Renames the file from the old name to the new name.

If the command line arguments are not valid or incomplete, an error message is displayed with the correct usage instructions.

## Logging

The script uses a decorator called `log_file_operation` to log file operations. Each operation is logged with the following details:

- Operation type: The type of operation performed (create or rename).
- File Path: The path of the file involved in the operation.
- Date and Time: The date and time when the operation occurred.
- Process ID: The ID of the process executing the operation.

For create and rename operations, the operation details are also written to the created or renamed file itself.


Feel free to ask if you have any questions or need further clarification!


**Powered by [TechAcademy](https://www.tech.edu.az/)**