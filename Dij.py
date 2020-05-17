
import math

class Graph:
    def __init__(self):
        self.root = None
        self.allPoints = []

class Point:
    def __init__(self, name):
        self.name = name
        self.connections = []
    
class Connection:
    def __init__(self, otherPoint, distance):
        self.otherPoint = otherPoint
        self.distance = distance
    def __repr__(self):
        return repr([self.otherPoint.name, self.distance])

class Visit:
    def __init__(self, prev, point, distance, currentCost):
        # distance here is this point's distance to the revious node
        # current cost is the complete path cost to this point from root
        self.prev = prev
        self.point = point
        self.distance = distance
        self.currentCost = currentCost

def shortestPaths(workingGraph):
    # get a list of nodes
    unvisitedNodes = []
    distances = []
    for i in workingGraph.allPoints:
        unvisitedNodes.append(i)
        # make a list of all graph points and inf distances
        newCon = Connection(i, math.inf)
        distances.append(newCon)
        
    # make a queue
    visitNext = []
    vn = Visit(None, workingGraph.root, 0, 0)
    visitNext.append(vn)
    curNode = visitNext[0]
    
    # traverse all points
    while len(visitNext) > 0:
        # pick the next node to visit
        distCheck = math.inf;
        for i in visitNext:
            if i.distance < distCheck:
                curNode = i
                distCheck = i.distance
        
        # update the current cost to get to the working node
        curCost = curNode.currentCost
        
        # check for lower connection costs
        for i in curNode.point.connections:
            nextDist = i.distance + curCost
            
            # get the point in distances
            objInDistances = None
            for d in distances:
                if d.otherPoint.name == i.otherPoint.name:
                    objInDistances = d
            
            # show relaxation process
            if nextDist < objInDistances.distance:
                print("relaxed " + objInDistances.otherPoint.name)
                print("was " + str(objInDistances.distance) )
                objInDistances.distance = nextDist
                print("is now " + str(objInDistances.distance) )
            # if this point is in unvisited points, add to visitNext
            addThis = 0
            for j in unvisitedNodes:
                if curNode.point.name == j.name:
                    addThis = 1
            if(addThis == 1):
                # add to nodes to visit
                newNode = Visit(curNode.point, i.otherPoint, i.distance, curCost + i.distance);
                visitNext.append(newNode)
        
        # remove current node from visitNext and unvisited nodes
        visitNext.remove(curNode)
        if curNode.point in unvisitedNodes:
            unvisitedNodes.remove(curNode.point)

    # make the root distance zero for aesthetic reasons
    for d in distances:
        if d.otherPoint.name == workingGraph.root.name:
            d.distance = 0;
    print(distances)

# points
A = Point("A")
B = Point("B")
C = Point("C")
D = Point("D")
E = Point("E")

# make graph
mainGraph = Graph()
mainGraph.allPoints.append(A)
mainGraph.allPoints.append(B)
mainGraph.allPoints.append(C)
mainGraph.allPoints.append(D)
mainGraph.allPoints.append(E)
mainGraph.root = A

# A connections
Con1 = Connection(B, 4)
A.connections.append(Con1)
Con2 = Connection(C, 2)
A.connections.append(Con2)

# B connections
Con3 = Connection(C, 3)
B.connections.append(Con3)
Con4 = Connection(D, 2)
B.connections.append(Con4)
Con5 = Connection(E, 3)
B.connections.append(Con5)

# C connections
Con6 = Connection(B, 1)
C.connections.append(Con6)
Con7 = Connection(D, 4)
C.connections.append(Con7)
Con8 = Connection(E, 5)
C.connections.append(Con8)

# D connections
# none

# E connections
Con9 = Connection(D, 1)
E.connections.append(Con9)

# listing out the connections
print ("List of connections: ")
print ("A: ")
print (A.connections)
print ("B: ")
print (B.connections)
print ("C: ")
print (C.connections)
print ("D: ")
print (D.connections)
print ("E: ")
print (E.connections)

# finding the shortest path costs for the root
print ("Finding shortest paths for root: ")
shortestPaths(mainGraph)
