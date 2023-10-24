import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import matplotlib as mpl 
import h5py
import cv2

# for i in range(1, 981):
#     file_name = f'data_{i:04d}.h5'

with h5py.File('patient002_frame12_slice_8.h5','r') as f:

    image = f['image'][:]
    # print(np.shape(image))
    # image = image[2,:,]
    print(np.shape(image))
    print(np.amax(image))
    print(np.amin(image))
    # print(np.unique(image))


    label = f['label'][:]
    # image = label[2,:,:]
    print(np.amax(label))
    print(np.amin(label))
    print(np.unique(label))


    scribble = f['scribble'][:]    
    # image = scribble[2,:,:]
    print(np.amax(scribble))
    print(np.amin(scribble))
    print(np.unique(scribble))

    # print(f'File {file_name}:')
    # print(f'Number of 0 pixels: {np.count_nonzero(scribble == 0)}')
    # print(f'Number of 1 pixels: {np.count_nonzero(scribble == 1)}')
    # print(f'Number of 2 pixels: {np.count_nonzero(scribble == 2)}')
    # print(f'Number of 255 pixels: {np.count_nonzero(scribble == 255)}')


    print('*'*10)
