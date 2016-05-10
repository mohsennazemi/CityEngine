'''
Created on Apr 20, 2016

@author: Mohsen
'''
'''''''''''''''''''''''
Pre-processing:
Name all the network's segment "segments"
'''''''''''''''''''''''

from scripting import *
import os.path

# get a CityEngine instance
ce = CE()

# obtaining segment, street, and sidewalks OIDs
ce.setSelection(ce.getObjectsFrom(ce.scene, ce.withName("segment")))
segments = ce.getObjectsFrom(ce.selection)

# Constructing OIDs, obtaining objects' vertices, and finding segment orientation
for i in segments:
    segmentsOID = ce.getOID(i)
    segment = ce.getVertices(ce.findByOID(segmentsOID))
    streetsOID = segmentsOID + ":0"
    street0 = ce.getVertices(ce.findByOID(streetsOID))
    sidewalks1OID = segmentsOID + ":1"
    sidewalk1 = ce.getVertices(ce.findByOID(sidewalks1OID))
    sidewalks2OID = segmentsOID + ":2"
    sidewalk2 = ce.getVertices(ce.findByOID(sidewalks2OID))

    # vertical, horizontal, or diagonal?
    if (segment[3] - segment[0])<=0.5: # 0.5 is the developer's tolerance value
        orientation = 'VERTICAL'
    elif (segment[5] - segment[2])<=0.5: # 0.5 is the developer's tolerance value
        orientation = 'HORIZONTAL'
    else:
        orientation = 'DIAGONAL'

    # obtaining common nodes between street and sidewalks
    street0 = [tuple(street0[3 * i:3 * i + 3]) for i in range(len(street0) // 3)]
    sidewalk1 = [tuple(sidewalk1[3 * i:3 * i + 3]) for i in range(len(sidewalk1) // 3)]
    sidewalk2 = [tuple(sidewalk2[3 * i:3 * i + 3]) for i in range(len(sidewalk2) // 3)]

    print "sidewalk1 tuple:", sidewalk1
    sidewalk3 = set(tuple(sidewalk1[3 * i:3 * i + 3]) for i in range(len(sidewalk1) // 3))
    print "sidewalk3_not tuple:", sidewalk3

    street0_set = set(street0)
    sidewalk1_set = set(sidewalk1)
    sidewalk2_set = set(sidewalk2)
    print "sidewalk1_set:", sidewalk1_set
    print ''

    intersection1 = list(street0_set.intersection(sidewalk1_set))
    intersection2 = list(street0_set.intersection(sidewalk2_set))
    #print intersection1

    #print "Segment ID: ", segmentsOID
    #print "Segments' vertices: ", segment
    #print "SEGMENT IS", orientation
    #print "Street and sidewalk 1 common points: ", intersection1
    #print "Street and sidewalk 2 common points: ", intersection2
    #print ''

    # eliminating the outlier points
    segments_midpoins = [(segment[0]+segment[3])/2, (segment[1]+segment[4])/2, (segment[2]+segment[5])/2]
    '''
    for j in intersection1:
        distance1 = (((segment[0]-intersection1[0])**2+(segment[1]-intersection1[1])**2+(segment[2]-intersection1[2])**2)**0.5)
        print distance1
    '''    



if __name__ == '__main__':
    pass 