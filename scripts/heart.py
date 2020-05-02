#!/usr/bin/env python3

import time
import sys

# TODO: fix this 
sys.path.append('../')

import raspi_hat

from sense_hat import SenseHat

if __name__ == "__main__":
    sense = SenseHat()
    renderer = raspi_hat.Renderer(sense,[0,0,0])

    positions = [[2,0],[3,0],[4,0],[5,1],[6,2],[7,3],[6,4],[5,5],[4,6],[3,6],[2,6],[1,5],[0,4],[1,3],[0,2],[1,1]]
    dots = [raspi_hat.Dot(pos,[255,0,0]) for pos in positions]
    nDots = len(dots)
    [renderer.add(dot) for dot in dots]
    j = 0
    while True:
        for i in range(len(renderer.entities)):
            if i == j:
                dot = renderer.entities[i]
                renderer.entities[i] = raspi_hat.Dot(dot.position, [0,0,0])
            else:
                dot = renderer.entities[i]
                renderer.entities[i] = raspi_hat.Dot(dot.position, [255,0,0])
        j = (j+1) % nDots
        renderer.render()
        time.sleep(0.05)
