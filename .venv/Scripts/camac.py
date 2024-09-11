import cv2

# Load the Haar cascades for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Check if the cascades are loaded correctly
if face_cascade.empty() or eye_cascade.empty():
    raise IOError('Could not load Haar cascades')

# Initialize the webcam
cap = cv2.VideoCapture(0)

blink_count = 0
eye_detected_prev = False

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame is captured correctly
    if not ret:
        print("Failed to capture image")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    eye_detected = False

    # Draw rectangles around the faces and detect eyes within the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect eyes within the face region
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) > 1:
            eye_detected = True
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    # Update blink count
    if eye_detected_prev and not eye_detected:
        blink_count += 1

    eye_detected_prev = eye_detected

    # Display verification status
    if blink_count >= 2:
        cv2.putText(frame, 'Human Verified', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    else:
        cv2.putText(frame, 'Human Not Verified', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Webcam - Eye Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()
