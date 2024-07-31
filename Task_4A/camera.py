import cv2
import time
labels = ['rehab', 'rehab', 'rehab', 'rehab', 'destroyedbuilding']
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
    leave = 0
    show_box = False
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

        # Resize the frame to fit the video window size
        frame = cv2.resize(frame, (video_width, video_height))

        # Display the frame
        cv2.imshow("Camera Feed", frame)

        # Check for key press, if 'a' is pressed, capture a frame
        key = cv2.waitKey(1)
        if key & 0xFF == ord('a'):
            print("Capturing image in 1 second...")
            time.sleep(1)
            # Capture a frame after 1 second
            ret, frame = cap.read()
            # Save the captured frame as an image
            if ret:
                cv2.imwrite("image.png", frame)
                print("Image captured and saved as 'image.png'")
                show_box = True
            else:
                print("Error: Unable to capture frame.")
                
        if ((leave == 1)or(key & 0xFF == ord('q'))):
                break 
        while show_box:
            # Draw boxes on the captured image
            print("Drawing boxes...")
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                leave = 1
                break 
            ret, frame = cap.read()      
            for i, (x, y, w, h) in enumerate(boxes):
                # x, y, w, h = box

                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, labels[i], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            frame = cv2.resize(frame, (video_width, video_height))
            # Display the frame with boxes
            cv2.imshow("Camera Feed", frame)
            cv2.waitKey(1)
                                   
    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
