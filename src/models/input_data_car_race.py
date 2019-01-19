# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import os
import numpy as np
import random

def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

class car_data():
    images=[]
    actions=[]
    rewards=[]
    def __init__(self,path='./'):
        data_directory=os.listdir(path)
        data_directory.remove('.gitkeep')
        print (data_directory)
        
        for element in data_directory:
            samples_files=os.listdir(path+'/'+element)
            for sample_file in samples_files:
                sample=np.load(path+'/'+element+'/'+sample_file)
                resized_image=rgb2gray(sample[0][:][:83]).ravel()
                self.images.append(resized_image)
                self.actions.append(sample[2])
                self.rewards.append(sample[1])
                
                
    def next_batch(self,batch_size=10):
                return random.sample(self.images,batch_size),'bite'
            
if __name__ == '__main__':
    test=car_data(path='./../../data/raw')

    #plt.imshow(test.images[0])
    x_train=test.next_batch()[0][0]
    #plt.imshow(x_train[0])
