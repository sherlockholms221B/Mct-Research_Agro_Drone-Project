import cv2
import torch 
from torchvision import transforms
from PIL import Image


@torch.no_grad()
def mask_image_with_objects(image_path, detected_objects):
    # Load the YOLOv5 model
    model = torch.hub.load('./cassava_yolov5.pt')

    # Load the image
    image = Image.open(image_path)

    # Perform object detection
    results = model(image)

    # Extract the bounding box coordinates of the detected objects
    bboxes = results.pandas().xyxy[0].values[:, :4].tolist()
    labels = results.pandas().xyxy[0].values[:, -1].tolist()

    # Read the image using OpenCV for masking
    image_cv = cv2.imread(image_path)

    # Iterate through the detected objects and apply masks
    for bbox, label in zip(bboxes, labels):
        # Extract the coordinates
        x_min, y_min, x_max, y_max = bbox

        # Create a mask for the object
        mask = np.zeros_like(image_cv)
        cv2.rectangle(mask, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (255, 255, 255), -1)

        # Apply the mask to the original image
        masked_image = cv2.bitwise_and(image_cv, mask)

        # Display the masked image
        cv2.imshow(f"Masked {label}", masked_image)
        cv2.waitKey(0)

    cv2.destroyAllWindows()

# Provide the path to your image
image_path = './data/images/test_640/G0018328.JPG'

# List of detected objects and their bounding box coordinates
detected_objects = [
    {'label': 'person', 'bbox': [100, 100, 200, 200]},  # Example detected object 1
    {'label': 'car', 'bbox': [300, 300, 400, 400]},     # Example detected object 2
    # Add more detected objects as needed
]

# Mask the image with the detected objects
mask_image_with_objects(image_path, detected_objects)
