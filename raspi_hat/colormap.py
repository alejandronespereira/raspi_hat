#!/usr/bin/env python3

import numpy as numpy

class ColorMap():
    def __init__(self):
        self._color_map = []

    def addColor(self,value,color):
        self._color_map.append((value,color))
        self._color_map.sort(key = lambda x : x[0])

    def getColor(self,value):
        assert(len(self._color_map) >= 2)

        lowerColors = [color for color in self._color_map if color[0] < value]
        upperColors = [color for color in self._color_map if color[0] >= value]
        
        if(len(lowerColors) == 0):
            return upperColors[0][1]
        if(len(upperColors) == 0):
            return lowerColors[-1]
        upperValue = upperColors[0][0]
        lowerValue = lowerColors[-1][0]

        alpha = (float(value) - float(lowerValue)) / (float(upperValue) - float(lowerValue))
        upperColor = upperColors[0][1]
        lowerColor = lowerColors[-1][1]
        color = [(1-alpha) * lower + alpha * upper for lower,upper in zip(lowerColor,upperColor)]
        return color
        