import argparse
import os
import sys
from src.detector import extract_plate
from src.ocr_engine import OCREngine
from src.logger import log_result

def process_image(img_path, ocr, output_csv):
    print(f"[INFO] Processing: {img_path}")
    try:
        plate_img = extract_plate(img_path)
        text, conf = ocr.recognize_text(plate_img)
        
        filename = os.path.basename(img_path)
        if output_csv:
            log_result(output_csv, filename, text, conf)
            
        print(f"[SUCCESS] Plate: {text} | Confidence: {conf:.2f}")
    except Exception as e:
        print(f"[ERROR] Failed to process {img_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Automated License Plate Recognition (ALPR) CLI")
    parser.add_argument('-i', '--input', type=str, help="Path to a single image file")
    parser.add_argument('-d', '--dir', type=str, help="Path to a directory of images for batch processing")
    parser.add_argument('-o', '--output', type=str, default="data/output_logs/results.csv", 
                        help="Path to output CSV file")
    
    args = parser.parse_args()
    
    if not args.input and not args.dir:
        parser.print_help()
        sys.exit(1)
        
    print("[INFO] Initializing OCR Engine (This may take a moment to load)...")
    ocr = OCREngine()
    
    if args.input:
        if not os.path.isfile(args.input):
            print(f"[ERROR] Input file not found: {args.input}")
            sys.exit(1)
        process_image(args.input, ocr, args.output)
        
    if args.dir:
        if not os.path.isdir(args.dir):
            print(f"[ERROR] Directory not found: {args.dir}")
            sys.exit(1)
            
        valid_exts = ('.png', '.jpg', '.jpeg')
        files = [f for f in os.listdir(args.dir) if f.lower().endswith(valid_exts)]
        
        print(f"[INFO] Found {len(files)} valid images in directory.")
        for f in files:
            full_path = os.path.join(args.dir, f)
            process_image(full_path, ocr, args.output)

if __name__ == "__main__":
    main()