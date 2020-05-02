#!/usr/bin/env python3

import time
import sys

# TODO: fix this 
sys.path.append('../')

import raspi_hat

from sense_hat import SenseHat

if __name__ == "__main__":
	sense = SenseHat()
	renderer = raspi_hat.Renderer(sense,[0,255,0])
	white = raspi_hat.Entity()
	white.matrix.setSolidColor([255,255,255])
	while(True):
		renderer.render(white)


	
