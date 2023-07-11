import cv2
import numpy as np
import random
from skimage.metrics import structural_similarity as compare_ssim

def salt_and_pepper_noise(img, dstSalt, dstPepper):

    density_salt = dstSalt
    density_pepper = dstPepper

    number_of_white_pixel = int(density_salt * (img.shape[0] * img.shape[1]))

    for i in range(number_of_white_pixel):
        y_coord = random.randint(0, img.shape[0]-1)
        x_coord = random.randint(0, img.shape[1]-1)
        img[y_coord][x_coord] = 255


    number_of_black_pixel = int(density_pepper * (img.shape[0] * img.shape[1]))

    for i in range(number_of_black_pixel):
        y_coord = random.randint(0, img.shape[0]-1)
        x_coord = random.randint(0, img.shape[1]-1)
        img[y_coord][x_coord] = 0

    return img

def find_max_ssim(noise_free_image, noisy_image):
    quality_range = []
    ssim_value_og = compare_ssim(noise_free_image, noisy_image)

    for i in range(3, 10, 2):
        denoise = cv2.medianBlur(noisy_image, i)
        ssim_value = compare_ssim(noise_free_image, denoise)
        quality_range.append(ssim_value)
    
    return max(quality_range), ssim_value_og

def denoiser(noise_free_image, noisy_image):

    filter_size = 1
    max_quality, ssim_value = find_max_ssim(noise_free_image, noisy_image)

    print(f"\nMax quality : {max_quality}")
    print(f"SSIM : {ssim_value}")

    filter_size = 1

    while ssim_value != max_quality:

        denoise = cv2.medianBlur(noisy_image, filter_size)
        ssim_value = compare_ssim(noise_free_image, denoise)

        print(f"SSIM after denoise by {filter_size} : {ssim_value}")

        compare_pics = np.concatenate((noise_free_image, denoise), axis=1)
        cv2.imshow(f'Original and Denoise {filter_size}', compare_pics)
        cv2.waitKey(1250)
        cv2.destroyAllWindows()

        filter_size += 2

    cv2.imwrite('pics/denoise.jpg', denoise)

    return 0


if __name__ == '__main__':

    image = cv2.imread('pics/DogCat.jpg', 0)
    density_salt = float(input("Enter salt density: "))
    density_paper = float(input("Enter paper density: "))

    noisy = salt_and_pepper_noise(image, density_salt, density_paper)
    cv2.imwrite('pics/noisy.jpg', noisy)
    
    noise_free_image = cv2.imread('pics/Dogcat.jpg', 0)
    noisy_image = cv2.imread('pics/noisy.jpg', 0)

    denoiser(noise_free_image, noisy_image)
    