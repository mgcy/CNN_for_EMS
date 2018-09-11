import statistics
import matplotlib.pyplot as plt
import numpy as np

original_image = np.loadtxt("D:\Academic\data_nvspl\\NVSPL_LAKE017_2010_12_02_00_image.txt")


def sigmoid(x):
    return 1 / (1 + np.exp(x))


sigmoid_image = sigmoid(original_image)
plt.imsave('D:\Academic\data_nvspl\\NVSPL_LAKE017_2010_12_02_00_image_sigm.jpg', sigmoid_image)


def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))


gaussian_image = gaussian(original_image, 20, 20)
plt.imsave('D:\Academic\data_nvspl\\NVSPL_LAKE017_2010_12_02_00_image_gaussian.jpg', gaussian_image)