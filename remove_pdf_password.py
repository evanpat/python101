import pikepdf
import os
import argparse


parser = argparse.ArgumentParser(description='Process some arguments.')
parser.add_argument('--file', type=str, help='File Path', required=False)
parser.add_argument('--dir', type=str, help='Directory', required=False)
parser.add_argument('--pw', type=str, help='Password', required=True)
args = parser.parse_args()

def has_password(file_path):
    try:
        with pikepdf.open(file_path) as pdf:
            return False

    except pikepdf.PasswordError:
        return True
    except Exception as e:
        raise

def remove_file_password(file_path, password):
    try:
        if has_password(file_path):
            # Open the protected PDF with the password
            with pikepdf.open(file_path, password=password) as pdf:
                # Save a new PDF without the password
                pdf.save(file_path + ".tmp")
            
            # Close the tmp file and Rename the file to original name
            os.remove(file_path)
            os.rename(file_path + ".tmp", file_path)
            print(f"Password removed for file: '{file_path}'")
        else:
            print(f"The file {file_path} doesn't have password")
        
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to rename '{file_path}'.")
    except pikepdf._core.PasswordError:
        print("Failed to open the PDF: incorrect password.")
    except Exception as e:
        print(f"An error occurred: {e}")


def remove_dir_password(directory, password):
    try:
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                remove_file_password(os.path.join(dirpath, filename), password)
                #print(os.path.join(dirpath, filename))
        
    except Exception as e:
        print(f"An error occurred: {e}")

if args.dir != None:
    remove_dir_password(args.dir, args.pw)
else:
    remove_file_password(args.file, args.pw)