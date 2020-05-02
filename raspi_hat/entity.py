#!/usr/bin/env python3

import raspi_hat

class Entity(): 

	def __init__(self):
		self._matrix = raspi_hat.Matrix()

	@property
	def matrix(self):
		return self._matrix

