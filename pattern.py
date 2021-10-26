import numpy as np
import matplotlib as plt


class Checker:

    def __init__(self, resolution, tile_size, output):
        self.resolution = resolution
        self.tile_size = tile_size
        self.output = output

    def draw(self):

        """
        here will be our numpy array for drawing the pattern
        """
        return self.output

    def show(self):

        """
        here we will visualize our pattern
        """


class Circle:

    def __init__(self, resolution, radius, position, output):
        self.resolution = resolution
        self.radius = radius
        self.position = position
        self.output = output

    def draw(self):

        """
        here will be our numpy array for drawing the pattern
        """
        return self.output

    def show(self):

        """
        here we will visualize our pattern
        """


class Spectrum:

    def __init__(self, resolution, output):
        self.resolution = resolution
        self.output = output

    def draw(self):
        """
        here will be our numpy array for drawing the pattern
        """
        return self.output

    def show(self):
        """
        here we will visualize our pattern
        """