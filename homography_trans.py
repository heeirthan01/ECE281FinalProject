import cv2
import os
import numpy as np

class ImageWithName:
    def __init__(self, image, name):
        self.image = image
        self.name = name

    def __repr__(self):
        return f"ImageWithName(name={self.name})"
    
    def __str__(self):
        return f"ImageWithName(name={self.name})"

def load_images_from_folder(folder):        
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        tmp = ImageWithName(img, filename)
        if img is not None:
            images.append(tmp)
    return images

def save_images(images, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    for i, img in enumerate(images):
        cv2.imwrite(os.path.join(folder, img.name), img.image)


def warp_image(img, H):
    image = img.image
    output_size = (image.shape[1], image.shape[0])  
    warped_image = cv2.warpPerspective(image, H, output_size, flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0))
    restored_image = cv2.warpPerspective(warped_image, np.linalg.inv(H), output_size, flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0))
    img.image = restored_image
    img.name = f'{img.name}'.replace('.png', '_warped.png').replace('.jpg', '_warped.jpg')
    return img


def compute_homography_matrix(src_points, dst_points):
    if src_points.shape[0] < 4 or dst_points.shape[0] < 4:
        raise ValueError("at least 4 points are required to compute homography")

    H, status = cv2.findHomography(src_points, dst_points, cv2.RANSAC)
    return H, status


src_pts = np.array([
    [100, 100],
    [200, 100],
    [200, 200],
    [100, 200]
], dtype=np.float32)

dst_pts = np.array([
    [110, 120],
    [210, 100],
    [220, 220],
    [120, 230]
], dtype=np.float32)

imgs = load_images_from_folder('example_images')

# H = np.array([[2.31320524,-9.04064327e-01, -3.26032166e+02],[5.65874219e-01,1.57498169e+00,-3.26032166e+02],[1.36785640e-03, -1.78844988e-04,1.00000000e+00]])
H, _ = compute_homography_matrix(src_pts, dst_pts)

warp_images = [warp_image(img, H) for img in imgs]

save_images(warp_images, 'warped_images')
