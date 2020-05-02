#!/usr/bin/env python3

from sense_hat import SenseHat

import numpy as np

class Renderer():
    def __init__(self,hat,background_color):
        
        self._hat = hat
        self._background_color = background_color
        self._pixels = np.zeros((8,8,3),np.uint8)
        self._pixels[:,:,:] = self._background_color

        self._entities = []
    def add(self,entity):
        self._entities.append(entity)

    @property
    def entities(self):
        return self._entities

    def render(self):
        renderedPixels = [self._background_color] *64 
        for entity in self._entities:

            pixelData = entity.matrix.data.reshape(64,3)
            mask = entity.matrix.mask.reshape(64)
            
            for i in range(len(pixelData)):
                m = mask[i]
                if not m:
                    continue
                p = pixelData[i]
                renderedPixels[i] = p
            
        self._hat.set_pixels(renderedPixels)
