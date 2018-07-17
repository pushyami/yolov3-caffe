###INSTALLING COCO API
#git clone https://github.com/cocodataset/cocoapi.git
#cd coco/PythonAPI
#make
#sudo make install
#sudo python setup.py install
#before doing above steps install cython


#%matplotlib inline
from pycocotools.coco import COCO
import numpy as np
import sys
import string
#import skimage.io as io
#import matplotlib.pyplot as plt
#import pylab
#pylab.rcParams['figur.figsize'] = (8.0, 10.0)

#TRAIN
f = open("yolotrain.txt", "w")
#TEST
#f = open("yolotest.txt", "w")

#Define the dataset and annotations file
dataDir = '/media/usb/'
#TRAIN
dataType = 'train2017'
annFile = '/media/usb/annotations/instances_train2017.json'
#TEST
#dataType = 'val2017'
#annFile = '/media/usb/annotations/instances_val2017.json'

#Initialize COCO api for instance annotations
coco = COCO(annFile)

#Display COCO categories
#cats = coco.loadCats(coco.getCatIds())
#for cat in cats:
#	print cat['name']

#Get all images
#imgs = coco.loadImgs(coco.getImgIds(coco.getAnnIds(iscrowd = None)))
#imgIds = coco.getImgIds()

#TRAIN
annsIds = coco.getAnnIds()
anns = coco.loadAnns(annsIds)
for img in anns:
	cat = img['category_id']
	imgid = img['image_id']
	f.write(dataDir + dataType + "/" + str(imgid).zfill(12) + ".jpg " + str(cat) + "\n")
	#print img['category_id']

#TEST
#annsIds = coco.getAnnIds()
#anns = coco.loadAnns(annsIds)
#for img in anns:
#       cat = img['category_id']
#       imgid = img['image_id']
#       f.write(dataDir + dataType + "/" + str(imgid).zfill(12) + ".jpg " + str(cat) + "\n")
       #print img['category_id']

