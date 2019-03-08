import os
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
train_path=r'C:\Users\Salman\Documents\Gender-Classification\train'
test_path=r'C:\Users\Salman\Documents\Gender-Classification\test'
valid_path=r'C:\Users\Salman\Documents\Gender-Classification\valid'

train_datagen=ImageDataGenerator()



train_batches=train_datagen.flow_from_directory(train_path,target_size=(224,224),classes=None,class_mode='categorical',batch_size=10)
test_batches=  train_datagen.flow_from_directory(test_path,target_size=(224,224),classes=None,class_mode='categorical',batch_size=10)
valid_batches= train_datagen.flow_from_directory(valid_path,target_size=(224,224),classes=None,class_mode='categorical',batch_size=10)

# plots images with labels within jupyter notebook


def plots(ims, figsize=(12,6), rows=1, interp=False, titles=None):
    if type(ims[0]) is np.ndarray:
        ims = np.array(ims).astype(np.uint8)
        if (ims.shape[-1] != 3):
            ims = ims.transpose((0,2,3,1))
    f = plt.figure(figsize=figsize)
    cols = len(ims)//rows if len(ims) % 2 == 0 else len(ims)//rows + 1
    for i in range(len(ims)):
        sp = f.add_subplot(rows, cols, i+1)
        sp.axis('Off')
        if titles is not None:
            sp.set_title(titles[i], fontsize=16)
        plt.imshow(ims[i], interpolation=None if interp else 'none')
imgs,labels=next(train_batches)
plots(imgs,titles=labels)


