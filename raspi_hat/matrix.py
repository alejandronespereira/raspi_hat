#!/usr/bin/env python3

import numpy as np

class Matrix():
	def __init__(self):
		self._data = np.zeros((8,8,3),np.uint8)
		self._mask = np.zeros((8,8),np.bool)

	@property
	def mask(self):
		return self._mask
	
	@property
	def data(self):
		return self._data
	
	def setSolidColor(self,color):
		self._data[:,:,:] = color
		self._mask[:,:] = True
	
	def setFull(self):
		self._mask[:,:] = True