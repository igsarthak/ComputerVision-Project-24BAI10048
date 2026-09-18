import csv
import os
from datetime import datetime

def log_result(csv_path, filename, plate_text, confidence):
    file_exists = os.path.isfile(csv_path)
    
    # Auto-generate the output directory if it doesn't exist
    os.makedirs(os.path.dirname(os.path.abspath(csv_path)), exist_ok=True)
    
    with open(csv_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Timestamp', 'Filename', 'Detected Plate', 'Confidence'])
            
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([timestamp, filename, plate_text, round(confidence, 4)])