import cv2
import easyocr
import matplotlib.pyplot as plt

image_path = r"C:\Users\nt465\OneDrive\Desktop\ANVR\photo1.png"

# read image
img = cv2.imread(image_path)

# instance text detector
reader = easyocr.Reader(['en'], gpu=False, verbose=False)

# detect text on image
results = reader.readtext(img)
print(results)

# Display the image with bounding boxes
for (bbox, text, prob) in results:
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))
    color = (0, 255, 0)  # Green color for bounding box
    cv2.rectangle(img, top_left, bottom_right, color, 2)
    cv2.putText(img, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

# Display the image with bounding boxes using matplotlib
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
