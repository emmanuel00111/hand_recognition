import cv2
# Start video capture
cam = cv2.VideoCapture(0)

# Create a named window
cv2.namedWindow("Hand Recognition App")

while True:
    ret, frame = cam.read()
    
    if not ret:
        print("Failed to grab frame")
        break

    # Display the captured frame
    cv2.imshow("Hand Recognition App", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()