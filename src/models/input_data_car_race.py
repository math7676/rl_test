# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import os
import numpy as np
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
                resized_image=sample[0][:][:83]
                self.images.append(resized_image)
                self.actions.append(sample[2])
                self.rewards.append(sample[1])
if __name__ == '__main__':
    test=car_data(path='./../../data/raw')

    plt.imshow(test.images[0])