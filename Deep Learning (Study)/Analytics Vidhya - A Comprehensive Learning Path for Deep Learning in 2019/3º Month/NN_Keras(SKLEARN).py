#!/usr/bin/env python
# coding: utf-8

# In[11]:


from sklearn.datasets import fetch_openml

mnist = fetch_openml('mnist_784')

X, Y = mnist['data'], mnist['target']

X.shape

