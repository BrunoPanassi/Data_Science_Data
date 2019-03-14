#!/usr/bin/env python
# coding: utf-8

# In[17]:


#Importing the libraries

get_ipython().run_line_magic('pylab', 'inline')
# it´s a line-oriented 'magic function' with the 'inline' as backend
import os
import numpy as np
import pandas as pd
from scipy.misc import imread #From scipy.misc i just want the imread
from sklearn.metrics import accuracy_score
import tensorflow as tf
import keras as k

#Setting a seed value to control the models randomness

seed = 128
rng = np.random.RandomState(seed) #rng it´s a instance of the class RandomState

#Seeting the directory paths, for safekeeping

root_dir = os.path.abspath('Path') #Create a folder in your directory
data_dir = os.path.join(root_dir, 'data') #Join folders in that directory
sub_dir  = os.path.join(root_dir, 'sub')

#Check if exists
os.path.exists(root_dir)
os.path.exists(data_dir)
os.path.exists(sub_dir)

#Loading and Preprocessing the data

#Convert to CSV
def convert(imgf, labelf, outf, n):
    f = open(imgf, "rb")
    o = open(outf, "w")
    l = open(labelf, "rb")

    f.read(16)
    l.read(8)
    images = []

    for i in range(n):
        image = [ord(l.read(1))]
        for j in range(28*28):
            image.append(ord(f.read(1)))
        images.append(image)

    for image in images:
        o.write(",".join(str(pix) for pix in image)+"\n")
    f.close()
    o.close()
    l.close()

#Converting
convert(os.path.join(data_dir, 'Train', 'train-images.idx3-ubyte'), os.path.join(data_dir, 'Train', 'train-labels.idx1-ubyte'), 'mnist_train.csv', 60000)
convert(os.path.join(data_dir, 'Test', 't10k-images.idx3-ubyte'),   os.path.join(data_dir, 'Test', 't10k-labels.idx1-ubyte'), 'mnist_test.csv', 10000)

#Reading the file
train_orig = pd.read_csv('mnist_train.csv')
test_orig = pd.read_csv('mnist_test.csv')

#Rename the files because the columns names don´t match
train_orig.rename(columns={'5':'label'}, inplace=True)
test_orig.rename(columns={'7':'label'}, inplace=True)

