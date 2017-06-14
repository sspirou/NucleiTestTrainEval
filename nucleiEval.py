import code
import sys
import os
import json
from pprint import pprint
import numpy as np

def getDistance(x1_coords,y1_coords,z1_coords,x2_coords,y2_coords,z2_coords):
	squared_dist = np.sum((x1_coords - x2_coords)**2 + (y1_coords-y2_coords)**2 + (z1_coords-z2_coords)**2)
	dist = np.sqrt(squared_dist)
	return dist

with open('Training1-Condition2.json') as data_file:	
	truthData = json.load(data_file)

with open('Test1-Pete-DAPI-Map2-Aldh1l1-Sox10.json') as data_file:
	testData = json.load(data_file)
	
truthPts = truthData["countingPoints"]
testPts = testData["countingPoints"]

pairs = []

for testPt in testPts:
	distances = []
	for pt in truthPts:
		dist = getDistance(testPt["x"],testPt["y"],testPt["z"],pt["x"],pt["y"],pt["z"])
		
		distances.append(dist)

	minDist = min(distances)
	pairPt = truthPts[distances.index(minDist)]
	pair = (testPt,pairPt)
	pairs.append(pair)

pprint(pairs)

correctCt = 0

for pair in pairs:
	if(pair[0]["color"]==pair[1]["color"]):
		correctCt+=1

print correctCt
print len(pairs)