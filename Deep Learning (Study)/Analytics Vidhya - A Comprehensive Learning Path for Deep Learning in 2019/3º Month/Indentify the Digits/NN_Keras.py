#!/usr/bin/env python
# coding: utf-8

# In[31]:


#Importing the libraries

get_ipython().run_line_magic('pylab', 'inline')
# it´s a line-oriented 'magic function' with the 'inline' as backend
import os
import numpy as np
import pandas as pd
from scipy.misc import imread #From scipy.misc i just want the imread
from sklearn.metrics import accuracy_score
import tensorflow as tf
import keras

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

