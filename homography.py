import cv2
import os
import numpy as np
from skimage import img_as_float, img_as_ubyte
from skimage.transform import swirl
from skimage.color import rgb2gray





def load_images_from_folder(folder):        
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images

def save_images(images, filenames, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    for img, filename in zip(images, filenames):
        base = os.path.basename(filename)
        cv2.imwrite(os.path.join(folder, base), img)


def warp_image(image, H):
<<<<<<< HEAD
    print('Orginal image shape:', image.shape)
    output_size = (image.shape[1]+100, image.shape[0]+100)  
=======
    output_size = (image.shape[1]+200, image.shape[0]+200)  
>>>>>>> 9bd2c5330126f656210f3cf81c825f51605cdae3
    warped_image = cv2.warpPerspective(image, H, output_size, flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0))
    restored_image = cv2.warpPerspective(warped_image, np.linalg.inv(H), output_size, flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0))
    return restored_image

imgs = load_images_from_folder('example_images')

<<<<<<< HEAD
#H = np.array([[2.31320524,-9.04064327e-01, -3.26032166e+02],[5.65874219e-01,1.57498169e+00,-3.26032166e+02],[1.36785640e-03, -1.78844988e-04,1.00000000e+00]])
#H = cv2.getAffineTransform(np.float32([[0, 0], [1, 0], [0, 1]]), np.float32([[0, 0], [1, 0], [0, 1]]))
#H = np.eye(3, dtype=np.float32)

def rotate_image(img, angle):
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0,0,0))
    return rotated

rotate_images225 = [rotate_image(img, 225) for img in imgs]
#save_images(rotate_images225, [f for f in os.listdir('example_images')], 'rotated_images225')

#rot_warp_225 = [warp_image(img,np.eye(3, dtype=np.float32)) for img in rotate_images225]
#save_images(rot_warp_225, [f for f in os.listdir('example_images')], 'rotated_warped_images225')
#gblurred_images = [cv2.GaussianBlur(img, (15, 15), 200) for img in imgs]
#H = np.diag(np.random.uniform(0.5, 20, size=3).astype(np.float32))
#diag_check = [warp_image(img, H) for img in imgs]
#save_images(diag_check, 'diagonal_images')
downsampledhalves_imgs = [cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2))) for img in imgs]
resized_halvesimgs = [cv2.resize(img, (int(img.shape[1]*2), int(img.shape[0]*2))) for img in downsampledhalves_imgs]
#save_images(downsampledhalves_imgs,[f for f in os.listdir('example_images')],'downsamphalf_images')
save_images(resized_halvesimgs,[f for f in os.listdir('example_images')],'resizehalf_images')
#save_images(gblurred_images, 'gblurred_images')

=======
# H = np.array([[2.31320524,-9.04064327e-01, -3.26032166e+02],[5.65874219e-01,1.57498169e+00,-3.26032166e+02],[1.36785640e-03, -1.78844988e-04,1.00000000e+00]])
H = np.eye(3)  # Identity matrix for no transformation
>>>>>>> 9bd2c5330126f656210f3cf81c825f51605cdae3

