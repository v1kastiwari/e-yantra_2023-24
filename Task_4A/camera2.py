import cv2
import time

def main():
    # Open the default camera (usually the first camera connected)
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Unable to open camera.")
        return

    # Get the screen resolution
    screen_width = 1920  # Change this according to your screen resolution
    screen_height = 1080  # Change this according to your screen resolution

    # Calculate the width and height for the video window (left half of the screen)
    video_width = int(screen_width / 2)
    video_height = screen_height

    # Create a window to display the video feed
    cv2.namedWindow("Camera Feed", cv2.WINDOW_NORMAL)
    
    # Set the position and size of the window
    cv2.resizeWindow("Camera Feed", video_width, video_height)
    cv2.moveWindow("Camera Feed", 0, 0)  # Move window to the top-left corner

    # Define the boxes with their coordinates (x, y, w, h)
    boxes = [
        (294, 190, 35, 44), (369, 189, 21, 43), (565, 15, 70, 77), (47, 136, 54, 94), (209, 213, 28, 25)
    ]

    # Loop to continuously read frames from the camera and display them
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if the frame is read successfully
        if not ret:
            print("Error: Unable to read frame.")
            break

        # Draw boxes on the frame
        for box in boxes:
            x, y, w, h = box
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Resize the frame to fit the video window size
        frame = cv2.resize(frame, (video_width, video_height))

        # Display the frame
        cv2.imshow("Camera Feed", frame)

        # Check for key press, if 'q' is pressed, exit the loop
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break

        # Introduce a delay of 5 seconds
        if key & 0xFF == ord('a'):
            print("Capturing image in 5 seconds...")
            time.sleep(5)
            # Capture a frame after 5 seconds
            ret, frame = cap.read()
            # Save the captured frame as an image
            if ret:
                # Draw boxes on the captured image
                for i,(x,y,w,h) in enumerate(boxes):
                    x, y, w, h = box
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.imwrite("image.png", frame)
                print("Image captured and saved as 'image.png'")
            else:
                print("Error: Unable to capture frame.")

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
