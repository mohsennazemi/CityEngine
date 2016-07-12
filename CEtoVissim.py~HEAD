'''
Created on Apr 20, 2016

@author: Mohsen
'''
'''''''''''''''''''''''
Pre-processing:
Name all the network's segments "segment"
'''''''''''''''''''''''

from scripting import *
import os.path
import math
import operator

# get a CityEngine instance
ce = CE()

# obtaining segment, street, and sidewalks OIDs
ce.setSelection(ce.getObjectsFrom(ce.scene, ce.withName('segment')))
segments = ce.getObjectsFrom(ce.selection)

# Constructing OIDs, obtaining objects' vertices, and translation to global coordination
ii = 0
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

    # Obtaining common nodes between street and sidewalks

    segment012t = [tuple(segment012[3 * a:3 * a + 3]) for a in range(len(segment012) // 3)]
    street0t = [tuple(street0[3 * a:3 * a + 3]) for a in range(len(street0) // 3)]
    sidewalk1t = [tuple(sidewalk1[3 * a:3 * a + 3]) for a in range(len(sidewalk1) // 3)]
    sidewalk2t = [tuple(sidewalk2[3 * a:3 * a + 3]) for a in range(len(sidewalk2) // 3)]

    street0_set = set(street0t)
    sidewalk1_set = set(sidewalk1t)
    sidewalk2_set = set(sidewalk2t)

    intersection1 = list(street0_set.intersection(sidewalk1_set))
    intersection2 = list(street0_set.intersection(sidewalk2_set))
    intersections = intersection1 + intersection2

    # finding streets' start/end points by averaging pedestrian-street common points
    if len(intersection1) == 2 and len(intersection2) == 2:

        if (intersection1[0][0] + intersection1[0][1]) < (intersection1[1][0] + intersection1[1][1]):
            min_inter1 = [intersection1[0][0] , intersection1[0][1]]
            max_inter1 = [intersection1[1][0] , intersection1[1][1]]
        else:
            min_inter1 = [intersection1[1][0] , intersection1[1][1]]
            max_inter1 = [intersection1[0][0] , intersection1[0][1]]

        if (intersection2[0][0] + intersection2[0][1]) < (intersection2[1][0] + intersection2[1][1]):
            min_inter2 = [intersection2[0][0] , intersection2[0][1]]
            max_inter2 = [intersection2[1][0] , intersection2[1][1]]
        else:
            min_inter2 = [intersection2[1][0] , intersection2[1][1]]
            max_inter2 = [intersection2[0][0] , intersection2[0][1]]
    else:
        print 'No exact 4 points for street ID "', streetsOID, '"'

    start = [(min_inter1[0] + min_inter2[0]) / 2, (min_inter1[1] + min_inter2[1]) / 2]
    end = [(max_inter1[0] + max_inter2[0]) / 2, (max_inter1[1] + max_inter2[1]) / 2]

    street_width_start = math.sqrt((min_inter1[0] - min_inter2[0]) ** 2 + (min_inter1[1] - min_inter2[1]) ** 2)
    street_width_end = math.sqrt((max_inter1[0] - max_inter2[0]) ** 2 + (max_inter1[1] - max_inter2[1]) ** 2)

    # Vissim input generator
    print "LinksEnter[", ii, "] = Vissim.Net.Links.AddLink(0,", "'LINESTRING(", round(start[0], 1), round(start[1], 1), ",", round(end[0], 1), round(end[1], 1), ")',", "[3.5])"
    ii += 1
    #print 'segment ID:', '"', streetsOID, '"'
    #print 'start:', start
    #print 'end:', end, '\n'
    #print street_width_start
    #print street_width_end, '\n'

if __name__ == '__main__':
    pass

    '''
    # segment_line
    M = (segment012[4]-segment012[1])/(segment012[3]-segment012[0])

    # vertical, horizontal, or diagonal?
    if (segment012[3] - segment012[0]) == 0:
        orientation = 'VERTICAL'
    elif (segment012[4] - segment012[1]) == 0:
        orientation = 'HORIZONTAL'
    else:
        orientation = 'DIAGONAL'

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
    '''
    # Finding the projection of intersection points on the segment line (p1' and p2').

    if len(intersection1) == 2:
        # forming vectors e1 (segment vector), e2 (segment point to the first intersection point), and e3 (segment point to the second intersection point)
        e1 = [segment012[3]-segment012[0], segment012[4]-segment012[1]]
        e2 = [(intersection1[0][0] - segment012[0]), (intersection1[0][1] - segment012[1])]
        e3 = [(intersection1[1][0] - segment012[0]), (intersection1[1][1] - segment012[1])]
        # get dot product of e1.e2 and e1.e3
        valDp1 = sum(map(operator.mul, e1, e2))
        valDp2 = sum(map(operator.mul, e1, e3))
        # get length of the vectors
        lenLineE1 = math.sqrt(e1[0] ** 2 + e1[1] ** 2)
        lenLineE2 = math.sqrt(e2[0] ** 2 + e2[1] ** 2)
        lenLineE3 = math.sqrt(e3[0] ** 2 + e3[1] ** 2)
        # cosign of the angle between vectors e1^e2 and e1^e3
        cos1 = valDp1 / (lenLineE1 * lenLineE2)
        cos2 = valDp2 / (lenLineE1 * lenLineE3)
        # length of v1p1' and v1p2'
        projLenOfLine1 = cos1 * lenLineE2
        pp1 = [((segment012[0] + (projLenOfLine1 * e1[0]) / lenLineE1)), ((segment012[1] + (projLenOfLine1 * e1[1]) / lenLineE1))]
        pp1_2 = [((valDp1 / (lenLineE1 * lenLineE2)) * lenLineE2 * e1[0] / lenLineE1), ((valDp1 / (lenLineE1 * lenLineE2)) * lenLineE2 * e1[1] / lenLineE1)]
        projLenOfLine2 = cos2 * lenLineE3
        pp2 =[((segment012[0] + (projLenOfLine2 * e1[0]) / lenLineE2)), ((segment012[1] + (projLenOfLine2 * e1[1]) / lenLineE2))]
        pp2_2 = [((valDp2 / (lenLineE1 * lenLineE3)) * lenLineE3 * e1[0] / lenLineE1), ((valDp2 / (lenLineE1 * lenLineE3)) * lenLineE3 * e1[1] / lenLineE1)]

    elif len(intersection2) == 2:
        # forming vectors e1 (segment vector), e2 (segment point to the first intersection point), and e3 (segment point to the second intersection point)
        e1 = [segment012[3]-segment012[0], segment012[4]-segment012[1]]
        e2 = [(intersection2[0][0] - segment012[0]), (intersection2[0][1] - segment012[1])]
        e3 = [(intersection2[1][0] - segment012[0]), (intersection2[1][1] - segment012[1])]
        # get dot product of e1.e2 and e1.e3
        valDp1 = sum(map(operator.mul, e1, e2))
        valDp2 = sum(map(operator.mul, e1, e3))
        # get length of the vectors
        lenLineE1 = math.sqrt(e1[0] ** 2 + e1[1] ** 2)
        lenLineE2 = math.sqrt(e2[0] ** 2 + e2[1] ** 2)
        lenLineE3 = math.sqrt(e3[0] ** 2 + e3[1] ** 2)
        # cosign of the angle between vectors e1^e2 and e1^e3
        cos1 = valDp1 / (lenLineE1 * lenLineE2)
        cos2 = valDp2 / (lenLineE1 * lenLineE3)
        # length of v1p1' and v1p2'
        projLenOfLine1 = cos1 * lenLineE2
        pp1_2 = [((segment012[0] + (projLenOfLine1 * e1[0]) / lenLineE1)), ((segment012[1] + (projLenOfLine1 * e1[1]) / lenLineE1))]
        projLenOfLine2 = cos2 * lenLineE3
        pp2_2 =[((segment012[0] + (projLenOfLine2 * e1[0]) / lenLineE2)), ((segment012[1] + (projLenOfLine2 * e1[1]) / lenLineE2))]

    else:
        print "No adjacent node on the sidewalk was found!"

    print 'segment:', segment012
    print 'intersection1:', intersection1
    print 'intersection2:', intersection2
    print 'e1, e2, e3:', e1, e2, e3
    #print 'lenLineE1, lenLineE2, lenLineE3:', lenLineE1, lenLineE2, lenLineE3
    #print 'cos1, cos2', cos1, cos2
    #print 'projLenOfLine1, projLenOfLine2:', projLenOfLine1, projLenOfLine2
    print 'pp1:', pp1
    print 'pp2:', pp2
    print 'pp1_2:', pp1_2
    print 'pp2_2:', pp2_2, '\n'
    '''

    # for m in distances:
        #if distances.count(m) == 1:
        #distances.remove(m)
        #print distances
