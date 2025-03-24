import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to perform face detection and gender estimation
def detect_faces_and_gender(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Iterate through detected faces
    for (x, y, w, h) in faces:
        # Draw rectangle around the face
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Estimate gender based on face size
        if h > w:  # Assume taller faces are female
            gender = "Female"
        else:     # Assume wider faces are male
            gender = "Male"
        
        # Display gender label
        cv2.putText(image, gender, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2, cv2.LINE_AA)

    return image

# Main function
def main():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Read frame from webcam
        ret, frame = cap.read()

        # Perform face detection and gender estimation
        frame_with_faces = detect_faces_and_gender(frame)

        # Display the frame with detected faces and gender estimation
        cv2.imshow('Face Detection & Gender Estimation', frame_with_faces)

        # Check for key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Entry point
if __name__ == "__main__":
    main()
