import os
import cv2

def convert_to_yolo_format(image_width, image_height, x_min, y_min, x_max, y_max):
    x_center = (x_min + x_max) / 2 / image_width
    y_center = (y_min + y_max) / 2 / image_height
    width = (x_max - x_min) / image_width
    height = (y_max - y_min) / image_height
    return x_center, y_center, width, height

annotations_file = '/home/martin/repos/garrafas/cylinder/test/_annotations.txt'
images_dir = '/home/martin/repos/garrafas/cylinder/test/'

with open(annotations_file, 'r') as f:
    lines = f.readlines()

for line in lines:
    parts = line.strip().split()
    image_file = parts[0]
    try:
        coords = list(map(int, parts[1].split(',')))
        x_min, y_min, x_max, y_max, class_id = coords

        # Load the image to get its dimensions
        image_path = os.path.join(images_dir, image_file)
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: No se pudo cargar la imagen {image_path}")
            continue
        image_height, image_width = image.shape[:2]

        # Convert coordinates to YOLO format
        x_center, y_center, width, height = convert_to_yolo_format(image_width, image_height, x_min, y_min, x_max, y_max)

        # Create the corresponding .txt file
        txt_file = os.path.splitext(image_file)[0] + '.txt'
        txt_path = os.path.join(images_dir, txt_file)
        with open(txt_path, 'w') as txt_f:
            txt_f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")
    except Exception as e:
        print(f"Error: {e}")
        continue