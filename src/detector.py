import cv2
import imutils
import numpy as np

def extract_plate(image_path):
    """
    Reads an image, applies edge detection, and crops the license plate contour.
    """
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not read image: {image_path}")
        
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Noise reduction and edge detection
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17) 
    edged = cv2.Canny(bfilter, 30, 200)
    
    # Find contours and sort by area
    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    
    location = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx
            break
            
    # Fallback: if no 4-point contour is found, return the original image for raw OCR
    if location is None:
        return img
        
    # Create mask to crop out the polygon
    mask = np.zeros(gray.shape, np.uint8)
    cv2.drawContours(mask, [location], 0, 255, -1)
    
    (y_coords, x_coords) = np.where(mask == 255)
    if len(y_coords) == 0 or len(x_coords) == 0:
        return img
        
    (y1, x1) = (np.min(y_coords), np.min(x_coords))
    (y2, x2) = (np.max(y_coords), np.max(x_coords))
    
    # Crop the exact plate dimensions
    cropped_plate = img[y1:y2+1, x1:x2+1]
    return cropped_plate