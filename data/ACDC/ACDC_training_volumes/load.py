import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import matplotlib as mpl 
import h5py
import cv2


filename = 'patient006_frame01.h5'


with h5py.File(filename,'r') as f:

	image = f['image'][:]
	print(np.shape(image))
	image = image[3,:,:]
	# image = cv2.resize(image,(224,224),interpolation=cv2.INTER_CUBIC)
	plt.imshow(image, cmap='gray', vmin=0, vmax=1)
	plt.xticks([])
	plt.yticks([])
	plt.savefig('img{}.png'.format(filename))



	image = f['label'][:]
	image = image[3,:,:]
	# image = cv2.resize(image,(224,224),interpolation=cv2.INTER_CUBIC)
	plt.imshow(image, cmap='gray', vmin=0, vmax=3)
	plt.xticks([])
	plt.yticks([])
	plt.savefig('label{}.png'.format(filename))




	scribble = f['scribble'][:]	
	image = scribble[3,:,:]
	image = cv2.resize(image,(224,224),interpolation=cv2.INTER_CUBIC)
	plt.imshow(image, cmap='gray', vmin=0, vmax=4)
	plt.xticks([])
	plt.yticks([])
	plt.savefig('scribble{}.png'.format(filename))