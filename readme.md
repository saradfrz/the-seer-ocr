# Image to Text Converter

This Python script extracts text from images using the Tesseract OCR (Optical Character Recognition) engine. It processes image files in a specified folder and saves the extracted text into separate text files.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x (Tested with Python 3.10)
- Tesseract OCR engine (Installed via `sudo apt install tesseract-ocr`)
- Python virtual environment (Optional but recommended)
- Required Python packages (Installed via `pip install -r requirements.txt`)

## Setup

1. Clone this repository or download the script file (`image_to_text_converter.py`).
2. Navigate to the project directory in your terminal.
3. Set up a Python virtual environment:
    ```bash
    python3.10 -m venv .venv
    source .venv/bin/activate
    ```
4. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
5. Place your input images in a folder named `input` within the project directory.

## Usage

Run the main script `image_to_text_converter.py`:

```bash
python image_to_text_converter.py
```

The script will process each image file in the `input` folder and save the extracted text into separate text files within an `output` folder.

## Supported Image Formats

The script supports the following common image formats:
- PNG
- JPEG
- JPG
- BMP
- GIF

## Troubleshooting

If you encounter any issues while running the script, ensure that:
- Tesseract OCR is properly installed.
- The input images are in one of the supported formats.
- Python and required packages are correctly installed and configured.