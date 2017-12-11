import os
import matplotlib.pyplot as plt
from scipy.misc import imresize

# root path depends on your computer
root = 'lfw/'                    #location of the LFW dataset
save_root = 'data/resized/'	 #directory to save the resized image
resize_size = 64

if not os.path.isdir(save_root):
    os.mkdir(save_root)
if not os.path.isdir(save_root + 'LFW'):
    os.mkdir(save_root + 'LFW')
dir_list = os.listdir(root)


for j in (dir_list):
    img_list = os.listdir(root+j)
    print img_list
    for i in range(len(img_list)):
        img = plt.imread(root+j+'/' + img_list[i])
        img = imresize(img, (resize_size, resize_size))
        plt.imsave(fname=save_root + 'LFW/' + img_list[i], arr=img)

        if (i % 500) == 0:
            print('%d images complete' % i)

