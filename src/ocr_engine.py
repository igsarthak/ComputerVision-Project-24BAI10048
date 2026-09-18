import easyocr

class OCREngine:
    def __init__(self):
        # Setting gpu=False ensures it runs on any machine; switch to True if CUDA is available.
        self.reader = easyocr.Reader(['en'], gpu=False)
        
    def recognize_text(self, image):
        # readtext accepts raw numpy arrays directly from OpenCV
        results = self.reader.readtext(image)
        if not results:
            return "NO_TEXT_FOUND", 0.0
            
        best_text = ""
        best_conf = 0.0
        
        for (bbox, text, conf) in results:
            # Clean string to keep only alphanumeric characters
            cleaned = "".join(e for e in text if e.isalnum())
            if conf > best_conf and len(cleaned) > 3:
                best_conf = conf
                best_text = cleaned
                
        # Fallback if aggressive cleaning removed the text
        if not best_text and results:
            best_text = results[0][1]
            best_conf = results[0][2]
            
        return best_text.upper(), best_conf