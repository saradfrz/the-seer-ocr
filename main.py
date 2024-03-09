import pytesseract
from PIL import Image
import os

# Path to the folder containing the input images
folder_path = "input"

# List to store file names
file_names = []

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        file_names.append(filename)

# Iterate over each image file
for img in file_names:
    # Construct the full path to the image file
    image_path = os.path.join(folder_path, img)
    
    # Check if the file is an image file (supports common image formats)
    if img.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # Use pytesseract to extract text from the image
        try:
            text = pytesseract.image_to_string(image_path, lang='eng')
            # Write the extracted text to a text file
            with open(f"output/{img.replace('.', '_')}.txt", 'w') as file:
                file.write(text)
            print(f"{img}: Text saved")
        except Exception as e:
            print(f"Error processing {img}: {e}")
    else:
        print(f"Skipping {img}: Not a supported image file format")

