import cv2
import numpy as np
import os
from random import shuffle
from tqdm import tqdm

TRAIN_DIR ='C:\\Users\\Salman\\Documents\\dogandcat\\train'
TEST_DIR='C:\\Users\\Salman\\Documents\\dogandcat\\test'
IMG_SIZE =50
LR =1e-3

MODEL_NAME = 'dogsvscats-{}-{}.model'.format(LR,'6conv-basic-video') 
#dog.93.png
def label_img(img):
    word_label = img.split('.')[-3]
    if word_label =='cat':return[1,0]
    elif word_label =='dog':return[0,1]
    
def create_train_data():
    training_data=[]
    for img in tqdm(os.listdir(TRAIN_DIR)):
        label=label_img(img)
        path = os.path.join(TRAIN_DIR,img)
        img = cv2.resize( cv2.imread(path,cv2.IMREAD_GRAYSCALE) , (IMG_SIZE,IMG_SIZE) )
        training_data.append([np.array(img), np.array(label)])
    shuffle(training_data)
    np.save('training_data.npy',training_data)
    return training_data

def process_test_data():
    testing_data=[]
    for img in tqdm(os.listdir(TEST_DIR)):
        img_num = img.split('.')[0]
        img=cv2.resize( cv2.imread(path,cv2.IMREAD_GRAYSCALE) , (IMG_SIZE,IMG_SIZE) )
        training_data.append([np.array(img), img_num])
    np.save('test_data.npy',testing_data)
    return testing_data

train_data= create_train_data()
#if youalready hauve data
#train_data =np.load('training_data.npy')
#it will load all the image of cat and dogs

import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression

import tensorflow as tf
tf.reset_default_graph()

convnet = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 1], name='input')

convnet = conv_2d(convnet, 32, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)

convnet = conv_2d(convnet, 64, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)

convnet = conv_2d(convnet, 32, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)

convnet = conv_2d(convnet, 64, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)

convnet = conv_2d(convnet, 32, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)

convnet = conv_2d(convnet, 64, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)

convnet = fully_connected(convnet, 1024, activation='relu')
convnet = dropout(convnet, 0.8)

convnet = fully_connected(convnet, 2, activation='softmax')
convnet = regression(convnet, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')

model = tflearn.DNN(convnet, tensorboard_dir='log')


if os.path.exists('{}.meta'.format(MODEL_NAME)):
    model.load(MODEL_NAME)
    print('model loaded!')
    
train = train_data[:-500]
test = train_data[-500:]

# x for feature y for label
X = np.array([i[0] for i in train]).reshape(-1,IMG_SIZE,IMG_SIZE,1)
Y = [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(-1,IMG_SIZE,IMG_SIZE,1)
test_y = [i[1] for i in test]

model.fit({'input': X}, {'targets': Y}, n_epoch=5, validation_set=({'input': test_x}, {'targets': test_y}), 
    snapshot_step=500, show_metric=True, run_id=MODEL_NAME)


model.save(MODEL_NAME)





        
        

    