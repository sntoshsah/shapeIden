import cv2
import numpy as np


def detect_shapes(image: np.ndarray):
    shapes = []
    
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Detect edges
    edges = cv2.Canny(blurred, 50, 150)
    
    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        x, y, w, h = cv2.boundingRect(approx)
        
        # Shape detection based on the number of vertices
        shape_name = "Unknown"
        num_vertices = len(approx)
        
        if num_vertices == 3:
            shape_name = "Triangle"
        elif num_vertices == 4:
            aspect_ratio = w / float(h)
            shape_name = "Square" if 0.9 <= aspect_ratio <= 1.1 else "Rectangle"
        elif num_vertices > 4:
            shape_name = "Circle"
        
        # Get color at the center of the shape
        center_x, center_y = x + w // 2, y + h // 2
        color_bgr = image[center_y, center_x].tolist()
        color = f"rgb({color_bgr[2]},{color_bgr[1]},{color_bgr[0]})"
        
        # Draw and label the detected shape
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
        cv2.putText(image, shape_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # Append detected shape data
        shapes.append({
            "name": shape_name,
            "coordinate": {"x": float(center_x), "y": float(center_y)},
            "color": color
        })
    
    return shapes, image
