import cv2

# Global variables
drawing = False  # True if mouse is pressed
ix, iy = -1, -1  # Initial coordinates

# Mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        width, height = x - ix, y - iy
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
        dimensions.append((ix, iy, width, height))
        cv2.imshow('image', img)

# Read an image from file
img = cv2.imread(r'image.png')

# Create a window and set the callback function
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)

dimensions = []

while len(dimensions) < 5:
    cv2.imshow('image', img)

    # Press 'esc' key to exit
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()

# Print recorded dimensions
for i, (x, y, w, h) in enumerate(dimensions, 1):
    print(f"Box {i}: (x={x}, y={y}, w={w}, h={h})")

# Return the list of dimensions
print("List of Dimensions:", dimensions)