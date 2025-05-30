import cv2
import os
import numpy as np

def load_images_from_folder(folder):        
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images

def save_images(images, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    for i, img in enumerate(images):
        cv2.imwrite(os.path.join(folder, f'warped_image_{i}.png'), img)


def warp_image(image, H):
    output_size = (image.shape[1]+200, image.shape[0]+200)  
    warped_image = cv2.warpPerspective(image, H, output_size, flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0))
    restored_image = cv2.warpPerspective(warped_image, np.linalg.inv(H), output_size, flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0))
    return restored_image

imgs = load_images_from_folder('example_images')

# H = np.array([[2.31320524,-9.04064327e-01, -3.26032166e+02],[5.65874219e-01,1.57498169e+00,-3.26032166e+02],[1.36785640e-03, -1.78844988e-04,1.00000000e+00]])
H = np.eye(3)  # Identity matrix for no transformation

warp_images = [warp_image(img, H) for img in imgs]


save_images(warp_images, 'warped_images')
