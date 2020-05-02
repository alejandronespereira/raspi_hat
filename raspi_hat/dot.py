#!/usr/bin/env python3

import raspi_hat
from raspi_hat import Entity

class Dot(Entity):
    def __init__(self, position = [0,0], color = [255,255,255]):

        Entity.__init__(self)

        self._limits = [0,7]
        assert(len(position) == 2)
        assert(position is not None)
        assert(self.isInLimits(position[0]) and self.isInLimits(position[1]))
        
        assert(len(color) == 3)
        assert(color is not None)
        assert(color[0] >= 0 and position[1] >= 0 and color[2] >= 0)
        assert(color[0] <= 256 and color[1] <= 255 and color[2] <= 255)     

        self._position = position
        self._color = color
        self._matrix.mask[:,:] = False
        self._matrix.mask[position[0],position[1]] = True

        self.matrix.data[position[0],position[1]] = self._color

    @property
    def color(self):
        return self._color

    @property
    def position(self):
        return self._position
    

    def setColor(self,color):
        self.matrix.data[self._position[0],self._position[1]] = self._color


    def isInLimits(self,value):
        return value >= self._limits[0] and value <= self._limits[1]

    def placeAt(self,new_position):
        x = max(min(new_position[0],8),0)
        y = max(min(new_position[1],8),0)
        
        self._position = [x,y]
        self.update()

    def update(self):
        self._matrix.mask[:,:] = False
        self._matrix.mask[self._position[0],self._position[1]] = True
        self.setColor(self._color)
