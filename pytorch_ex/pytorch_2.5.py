import os
import torch
import pandas as pd
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

import warnings

warnings.filterwarnings("ignore")

plt.ion()

landmarks_frame = pd.read_csv("D:/scidata/faces/face_landmarks.csv")

n = 65
img_name = landmarks_frame.iloc[n, 0]
lanmarks = landmarks_frame.iloc[n, 1:].as_matrix()
lanmarks = lanmarks.astype('float').reshape(-1, 2)

print('Image name: {}'.format(img_name))
print('Landmarks shape: {}'.format(lanmarks.shape))
print('First 4 Landmarks: {}'.format(lanmarks[:4]))


def show_landmarks(image, landmarks):
    plt.imshow(image)
    plt.scatter(lanmarks[:, 0], lanmarks[:, 1], s=10, marker='.', c='r')
    plt.pause(0.001)


plt.figure()
show_landmarks(io.imread('D:/scidata/faces', img_name), lanmarks)
plt.show()

