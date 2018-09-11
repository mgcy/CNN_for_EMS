import matplotlib.pyplot as plt
from pylab import figure
from PIL import Image, ImageDraw
import numpy as np
import cv2
from scipy import ndimage

f1 = open("D:\Academic\data_nvspl\LAKE017\\NVSPL_LAKE017_2010_12_02_18.txt", "r")
f2 = open("D:\Academic\data_nvspl\\NVSPL_LAKE017_2010_12_02_18_image.txt", 'w')
next(f1)
for line1 in f1:
    line2 = line1.split(',')[2:35]
    for item in line2:
        f2.write(item + ' ')
    f2.write('\n')
f1.close()
f2.close()

my_data = np.loadtxt('D:\Academic\data_nvspl\\NVSPL_LAKE017_2010_12_02_18_image.txt')
list1 = [5]
list2 = [111]
len_image = 350
plt.imshow(my_data[2700:2850])
for i1 in range(len(list1)):
    plt.axhline(list1[i1], color='r', linestyle='dashed', linewidth=2)
    plt.axhline(list1[i1] + list2[i1], color='r', linestyle='dashed', linewidth=2)
# cv2.imwrite('D:\Academic\data_nvspl\\NVSPL_LAKE017_2010_12_02_00_image.png',new_image)
# plt.savefig('D:\Academic\data_nvspl\\NVSPL_LAKE017_2010_12_02_00_image.png', format='png', dpi=2000)
plt.imsave('D:\Academic\data_nvspl\\NVSPL_LAKE017_2010_12_02_00_image.jpg', my_data[0:len_image])
# rotated_img = ndimage.rotate(my_data[:280],90)
# plt.imshow(rotated_img)
