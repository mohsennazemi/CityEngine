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
ce.setSelection(ce.getObjectsFrom(ce.scene, ce.withName('segment')))
segments = ce.getObjectsFrom(ce.selection)

# Constructing OIDs, obtaining objects' vertices, translation to global coordination, and finding segment orientation
for i in segments:

    segmentsOID = ce.getOID(i)
    segment_init = ce.getVertices(ce.findByOID(segmentsOID))
    segment012 = []
    for j in range(0, len(segment_init), 3):
        x012 = segment_init[j]
        y012 = segment_init[j+1]
        z012 = (-1)*segment_init[j+2]
        segment012.extend([x012, z012, 0.0])

    streetsOID = segmentsOID + ':0'
    street0_init = ce.getVertices(ce.findByOID(streetsOID))
    street0 = []
    for k in range(0, len(street0_init), 3):
        x0 = street0_init[k]
        y0 = street0_init[k + 1]
        z0 = (-1) * street0_init[k + 2]
        street0.extend([x0, z0, 0.0])

    sidewalks1OID = segmentsOID + ':1'
    sidewalk1_init = ce.getVertices(ce.findByOID(sidewalks1OID))
    sidewalk1 = []
    for l in range(0, len(sidewalk1_init), 3):
        x1 = sidewalk1_init[l]
        y1 = sidewalk1_init[l + 1]
        z1 = (-1) * sidewalk1_init[l + 2]
        sidewalk1.extend([x1, z1, 0.0])

    sidewalks2OID = segmentsOID + ':2'
    sidewalk2_init = ce.getVertices(ce.findByOID(sidewalks2OID))
    sidewalk2 = []
    for m in range(0, len(sidewalk2_init), 3):
        x2 = sidewalk2_init[m]
        y2 = sidewalk2_init[m + 1]
        z2 = (-1) * sidewalk2_init[m + 2]
        sidewalk2.extend([x2, z2, 0.0])

    print segment012
    print street0
    print sidewalk1
    print sidewalk2, '\n'

    # vertical, horizontal, or diagonal?
    if (segment012[3] - segment012[0]) == 0:
        orientation = 'VERTICAL'
    elif (segment012[4] - segment012[1]) == 0:
        orientation = 'HORIZONTAL'
    else:
        orientation = 'DIAGONAL'

    street0_set = set(street0)
    sidewalk1_set = set(sidewalk1)
    sidewalk2_set = set(sidewalk2)

    intersection1 = list(street0_set.intersection(sidewalk1_set))
    intersection2 = list(street0_set.intersection(sidewalk2_set))
    intersections = intersection1 + intersection2

    # obtaining common nodes between street and sidewalks
    segment012 = [tuple(segment012[3 * i:3 * i + 3]) for i in range(len(segment012) // 3)]
    street0 = [tuple(street0[3 * i:3 * i + 3]) for i in range(len(street0) // 3)]
    sidewalk1 = [tuple(sidewalk1[3 * i:3 * i + 3]) for i in range(len(sidewalk1) // 3)]
    sidewalk2 = [tuple(sidewalk2[3 * i:3 * i + 3]) for i in range(len(sidewalk2) // 3)]

if __name__ == '__main__':
    pass

    '''
    # eliminating the outlier points for segments with more than 4 common points
    if len(intersections) > 4:

        segments_midpoints = [(segment[0]+segment[3])/2, (segment[1]+segment[4])/2, (segment[2]+segment[5])/2]
        distances1 = []
        distances2 = []

        for j in intersection1:
            distance1 = (((segments_midpoints[0]-j[0])**2+(segments_midpoints[1]-j[1])**2+(segments_midpoints[2]-j[2])**2)**0.5)
            distances1.append(distance1)
        #if len(distances1) > 2:

        for k in intersection2:
            distance2 = (((segments_midpoints[0]-k[0])**2+(segments_midpoints[1]-k[1])**2+(segments_midpoints[2]-k[2])**2)**0.5)
            distances2.append(distance2)

        distances = distances1 + distances2

        distance = None
        for n in distances:
            if distances.count(m) == 1:
                distance = n
    '''
    #for m in distances:
        #if distances.count(m) == 1:
        #distances.remove(m)
        #print distances
