import pygame,sys 
from pygame.locals import *
import numpy as np 
from keras.models import load_model
import cv2


WIN_SIZEX=600
WIN_SIZEY=450

#initialize 
pygame.init()
pygame.display.set_mode((WIN_SIZEX,WIN_SIZEY))