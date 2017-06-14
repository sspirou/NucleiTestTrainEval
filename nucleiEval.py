import sys
import os
import json
from pprint import pprint
import numpy as np

def getDistance(x1_coords,y1_coords,z1_coords,x2_coords,y2_coords,z2_coords):
    p1 = np.array([x1_coords, y1_coords, z1_coords])
    p2 = np.array([x2_coords, y2_coords, z2_coords])
    squared_dist = np.sum(p1**2 + p2**2, axis=0)
    dist = np.sqrt(squared_dist)
    return dist

with open('Training1-Condition2.json') as data_file:    
    truthData = json.load(data_file)

with open('Test1-Pete-DAPI-Map2-Aldh1l1-Sox10.json') as data_file:
    testData = json.load(data_file)
	
truthPts = truthData["countingPoints"]
testPts = testData["countingPoints"]

x1 = truthPts[0]["x"]
y1 = truthPts[0]["y"]
z1 = truthPts[0]["z"]
x2 = testPts[0]["x"]
y2 = testPts[0]["y"]
z2 = testPts[0]["z"]

print(getDistance(x1,y1,z1,x2,y2,z2))