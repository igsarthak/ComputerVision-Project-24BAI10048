# Computer Vision Project - 24BAI10048
### Automated License Plate Recognition (ALPR) Pipeline


---


## Student Information


| Field | Details |
|---|---|
| **Student Name** | *Sarthak Verma* |
| **Registration Number** | *24BAI10048* |
| **Language** | *Python* |
| **Domain** | *Artificial Intelligence & Machine Learning* |
| **Data Storage** | *Comma-Separated Values (.csv)* |


---


## About This Project

This repository contains the complete submission for the Automated License Plate Recognition (ALPR) Pipeline, a robust, console-based Python application designed to detect, extract, and log vehicle license plates from images. 

This project is a professional-grade Computer Vision application demonstrating end-to-end software engineering. It utilizes mathematical edge detection (Canny), morphological transformations, and contour analysis to isolate the rectangular shape of license plates without relying on heavy pre-trained cascade models. Optical Character Recognition (OCR) is then applied to extract alphanumeric text, and the results are persistently logged into a structured CSV file. The entire pipeline is executable via a robust Command-Line Interface (CLI).


---


## Repository Structure


    CV_Project/
    │
    ├── data/                                  -> Data storage & outputs
    │   ├── sample_images/                     -> Test input images (.jpg, .png)
    │   └── output_logs/                       -> Generated CSV files (results.csv)
    │
    ├── src/                                   -> Source code modules
    │   ├── __init__.py                        -> Package initializer
    │   ├── detector.py                        -> OpenCV vision logic
    │   ├── ocr_engine.py                      -> EasyOCR text extraction logic
    │   └── logger.py                          -> CSV formatting and persistence
    │
    ├── requirements.txt                       -> Python package dependencies
    └── main.py                                -> Primary CLI entry point


---


## Module Descriptions & Architecture


### 1. src.detector

The foundational computer vision logic for isolating the physical plate. 

- **extract_plate() :** Reads the image array, converts it to grayscale, applies bilateral filtering for noise reduction, and uses the Canny algorithm for edge detection. It mathematically approximates polygonal curves to locate the four-point contour of the license plate and returns a cropped numpy array.


### 2. src.ocr_engine

The text recognition layer.

- **OCREngine :** Initializes the EasyOCR reader. It accepts the cropped numpy array directly from the detector, extracts the raw text, filters out non-alphanumeric characters, and returns the most confident text string alongside its confidence score.


### 3. src.logger

The data persistence layer.

- **log_result() :** Isolated logic for saving detection results to the `data/output_logs/` directory. Automatically generates the CSV file with proper headers if it does not exist and appends timestamps, filenames, plate text, and confidence metrics. 


### 4. main.py (Main Application CLI)

The interaction layer and entry point.

- **Features :**
	- **Argument Parsing :** Uses the built-in `argparse` module to handle user inputs cleanly.
	- **Single Image Processing :** Allows the evaluation of one specific vehicle image via the `-i` flag.
	- **Batch Directory Processing :** Iterates through an entire folder of vehicle images sequentially using the `-d` flag.
	- **Custom Exporting :** Allows the user to dictate exactly where the CSV log is saved using the `-o` flag.


---


## How to Run the Application


### Prerequisites

- Python 3.10 or higher installed on your system.
- A terminal, command prompt, or PowerShell interface.


### Step 1 — Clone the repository

```bash
git clone https://github.com/igsarthak/ComputerVision-Project-24BAI10048.git
cd ComputerVision-Project-24BAI10048
```

### Step 2 — Install Dependencies

Ensure your environment is set up with the required libraries. This will automatically fetch the latest compatible versions of OpenCV and EasyOCR:
`pip install -r requirements.txt`


### Step 3 — Provide Test Data

Ensure you have placed at least one test vehicle image (e.g., `test_car.jpg`) inside the `data/sample_images/` directory.


### Step 4 — Run the Application

Execute the pipeline using the command-line interface. 

**To process a single image:**
`python main.py -i data/sample_images/test_car_image_name.jpg`

**To process a batch of images:**
`python main.py -d data/sample_images/`

### Step 5 — Review the Output
The terminal will display real-time extraction results and confidence scores. Navigate to `data/output_logs/results.csv` to view the persistently saved data ledger.


---


## Dependencies


| Dependency | Used For | Notes |
|---|---|---|
| `opencv-python` | Image processing & Contours | Core computer vision library |
| `easyocr` | Optical Character Recognition | Extracts alphanumeric text from crops |
| `numpy` | Array manipulation | Required for handling image matrices |
| `imutils` | Contour sorting | Simplifies OpenCV contour extraction |


---


## Tested On

- Windows (PowerShell/Command Prompt)
- Python 3.13 Standard Execution Environment
