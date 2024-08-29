import qrcode
import cv2
from pyzbar.pyzbar import decode
from PIL import Image

def generate_qr_code(data, filename):
    """Generate a QR Code from the provided data and save it as an image."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")

def decode_qr_code_from_image(filename):
    """Decode a QR Code from an image file."""
    img = Image.open(filename)
    decoded_objects = decode(img)
    
    if decoded_objects:
        for obj in decoded_objects:
            print(f"Data in QR Code: {obj.data.decode('utf-8')}")
    else:
        print("No QR code found in the image.")

def decode_qr_code_from_camera():
    """Decode QR Code in real-time from camera feed."""
    cap = cv2.VideoCapture(0)
    
    while True:
        _, frame = cap.read()
        decoded_objects = decode(frame)
        
        for obj in decoded_objects:
            points = obj.polygon
            if len(points) > 4:
                hull = cv2.convexHull(points)
                points = hull

            for i in range(len(points)):
                pt1 = (points[i][0], points[i][1])
                pt2 = (points[(i + 1) % len(points)][0], points[(i + 1) % len(points)][1])
                cv2.line(frame, pt1, pt2, (255, 0, 0), 3)
            
            print(f"Data in QR Code: {obj.data.decode('utf-8')}")

        cv2.imshow('QR Code Scanner', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Example usage:
    
    # 1. Generate a QR code
    data = "https://www.example.com"
    filename = "example_qr.png"
    generate_qr_code(data, filename)
    
    # 2. Decode a QR code from an image
    decode_qr_code_from_image(filename)
    
    # 3. Decode QR codes in real-time from the camera feed
    decode_qr_code_from_camera()
