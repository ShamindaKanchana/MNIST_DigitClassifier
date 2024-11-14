import pygame,sys 
from pygame.locals import *
import numpy as np 
from keras.models import load_model
import cv2


WIN_SIZEX=600
WIN_SIZEY=450


WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)

IMAGESAVE=False

MODEL=load_model("model.h5")

LABELS={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}

#initialize 
pygame.init()
pygame.display.set_mode((WIN_SIZEX,WIN_SIZEY))

#FONT=pygame.font.Font('freesansbold.tff',18)
pygame.display.set_caption('Digit Board')
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()