#!/usr/bin/env python

import cv2
import sys
import caffe
import numpy
model = "./yolodeploy.prototxt"
weights = "./yolov3_weights.caffemodel"

caffe.set_mode_cpu()

net = caffe.Net(model, weights, caffe.TEST)
image = cv2.imread(sys.argv[1])
inputResImg = cv2.resize(image, (256, 256), interpolation=cv2.INTER_CUBIC)
transposedInputImg =inputResImg.transpose(2,0,1)
net.blobs['data'].data[...]=transposedInputImg
out = net.forward()

k = out["loss"]
#print k
count =-1
for x in numpy.nditer(k):
	count = count +1
	if x != 0:
		print x
		print count
print count
#for i in k:
#	print i

