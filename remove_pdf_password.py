import pikepdf
import os
import argparse


parser = argparse.ArgumentParser(description='Process some arguments.')
parser.add_argument('--file', type=str, help='File Path', required=True)
parser.add_argument('--pw', type=str, help='Password', required=True)

# Parse the arguments
args = parser.parse_args()

# Print the argument
print(f"The argument passed is: {args.file} {args.pw}")

# Specify the input and output PDF file paths
input_pdf_path = args.file
password = args.pw

try:
    # Open the protected PDF with the password
    with pikepdf.open(input_pdf_path, password=password) as pdf:
        # Save a new PDF without the password
        pdf.save(input_pdf_path + ".tmp")
    
    try:
    # Rename the file
        os.remove(input_pdf_path)
        os.rename(input_pdf_path + ".tmp", input_pdf_path)
        print(f"Password removed and saved as '{input_pdf_path}'")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_pdf_path}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to rename '{input_pdf_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

except pikepdf.PasswordError:
    print("Failed to open the PDF: incorrect password.")
except Exception as e:
    print(f"An error occurred: {e}")

