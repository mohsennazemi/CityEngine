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

# Constructing OIDs, obtaining objects' vertices, and finding segment orientation
for i in segments:
    segmentsOID = ce.getOID(i)
    segment = ce.getVertices(ce.findByOID(segmentsOID))
    streetsOID = segmentsOID + ':0'
    street0 = ce.getVertices(ce.findByOID(streetsOID))
    sidewalks1OID = segmentsOID + ':1'
    sidewalk1 = ce.getVertices(ce.findByOID(sidewalks1OID))
    sidewalks2OID = segmentsOID + ':2'
    sidewalk2 = ce.getVertices(ce.findByOID(sidewalks2OID))

    # vertical, horizontal, or diagonal?
    if (segment[3] - segment[0])<=0.5: # 0.5 is the developer's tolerance value
        orientation = 'VERTICAL'
    elif (segment[5] - segment[2])<=0.5: # 0.5 is the developer's tolerance value
        orientation = 'HORIZONTAL'
    else:
        orientation = 'DIAGONAL'

    # obtaining common nodes between street and sidewalks
    segment012 = [tuple(segment[3 * i:3 * i + 3]) for i in range(len(segment) // 3)]
    street0 = [tuple(street0[3 * i:3 * i + 3]) for i in range(len(street0) // 3)]
    sidewalk1 = [tuple(sidewalk1[3 * i:3 * i + 3]) for i in range(len(sidewalk1) // 3)]
    sidewalk2 = [tuple(sidewalk2[3 * i:3 * i + 3]) for i in range(len(sidewalk2) // 3)]

    street0_set = set(street0)
    sidewalk1_set = set(sidewalk1)
    sidewalk2_set = set(sidewalk2)

    intersection1 = list(street0_set.intersection(sidewalk1_set))
    intersection2 = list(street0_set.intersection(sidewalk2_set))
    intersections = intersection1 + intersection2

    #print "Segment ID: ", segmentsOID
    #print "Segments' vertices: ", segment
    #print "SEGMENT IS", orientation
    #print "Street and sidewalk 1 common points: ", intersection1
    #print "Street and sidewalk 2 common points: ", intersection2
    #print len(intersection1), len(intersection2)
    #print ''

    # eliminating the outlier points for segments with more than 4 common points
    if len(intersections) > 4:

        segments_midpoints = [(segment[0]+segment[3])/2, (segment[1]+segment[4])/2, (segment[2]+segment[5])/2]
        distances1 = []
        distances2 = []

        for j in intersection1:
            distance1 = (((segments_midpoints[0]-j[0])**2+(segments_midpoints[1]-j[1])**2+(segments_midpoints[2]-j[2])**2)**0.5)
            distances1.append(distance1)
        print 'distances1:',distances1
            #for m in distances1:
             #   if distances1.count(m) == 1:
              #      print 'hi', distances1
                    #distances1.remove(m)
                    #print distances1

        for k in intersection2:
            distance2 = (((segments_midpoints[0]-k[0])**2+(segments_midpoints[1]-k[1])**2+(segments_midpoints[2]-k[2])**2)**0.5)
            distances2.append(distance2)
        print 'distances2:',distances2
            #for n in distances2:
             #   if distances2.count(n) == 1:
              #      print 'bye', distances2
                    #distances2.remove(n)
                    #print distances2
        distances = distances1+distances2
'''
    # reporting segments with less than 2 common points with each of their associated sidewalks
    if len(intersection1) < 2:
        print 'Segment',segmentsOID,'has less than 2 points in common with its sidewalk1!'
        print intersection1
        print ''
    elif len(intersection2) < 2:
        print 'Segment',segmentsOID,'has less than 2 points in common with its sidewalk2!'
        print intersection2
        print ''
'''
if __name__ == '__main__':
    pass

    '''
        a=[4.5,4.5,5.3]
        for z in a:
            if a.count(z) == 3:
                print "hi"
'''