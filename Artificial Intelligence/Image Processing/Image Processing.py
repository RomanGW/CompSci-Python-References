"""
Robotics and Perception Assignment

This assignment covers introductory topics in Robotics within the field of AI, focusing on sensory processing,
computer vision, and motion planning and pathfinding algorithms.

Prior to starting, make sure to have the following libraries installed:
- OpenCV (cv2)
- numpy
- matplotlib

You can install them using pip:
pip install opencv-python numpy matplotlib
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def image_processing(image_path):
    """
    Load an image and apply basic processing techniques such as grayscale conversion,
    thresholding, and edge detection.

    Parameters:
    image_path (str): The file path to an image.

    Returns:
    processed_images (dict): A dictionary with keys 'grayscale', 'thresholded', and 'edges' corresponding
                             to the processed images.
    """
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    edges = cv2.Canny(gray, 100, 200)
    
    processed_images = {
        "grayscale" : gray,
        "thresholded" : thresh,
        "edges" : edges
        }
    return processed_images

def sensory_processing(sensor_data):
    """
    Process raw sensor data to detect obstacles in the environment.

    Parameters:
    sensor_data (list of float): Simulated distance sensor readings in an environment with obstacles.

    Returns:
    obstacles (list of int): Indices of the sensor readings that are classified as obstacles.
    """
    
    obstacle_threshold = 1.5
    obstacles = []

    for index, distance in enumerate(sensor_data):
        if distance < obstacle_threshold:
            obstacles.append(index)

    return obstacles

def pathfinding(grid, start, goal):
    """
    Implement a pathfinding algorithm (such as A* or Dijkstra's) to find a path from start to goal in a grid.

    Parameters:
    grid (numpy.ndarray): 2D array representing the grid where 0s are passable tiles and 1s are obstacles.
    start (tuple): Starting grid position as a tuple (row, column).
    goal (tuple): Goal grid position as a tuple (row, column).

    Returns:
    path (list): The path from start to goal as a list of tuples (row, column). Return an empty list if no path is found.
    """
    
    path = []
    
    return path

