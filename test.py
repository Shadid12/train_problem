from sys import getrecursionlimit, setrecursionlimit
from routes import Routes

# Graph: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
graph = {
          'A': {'B': 5, 'D': 5, 'E': 7 },
          'B': {'C': 4},
          'C': {'D': 8, 'E': 2},
          'D': {'C': 8, 'E':  6},
          'E': {'B': 3}
        }

r = Routes(graph)

def testDistanceBetween_ABC():
	assert r.distanceBetween(['A','B','C']) == 9
	
def testDistanceBetween_AD():
	assert r.distanceBetween(['A','D']) == 5
	
def testDistanceBetween_ADC():
	assert r.distanceBetween(['A','D','C']) == 13
	
def testDistanceBetween_AEBCD():
	assert r.distanceBetween(['A','E','B', 'C', 'D']) == 22
	
def testDistanceBetween_AED():
	assert r.distanceBetween(['A','E','D']) == 'There is no route'

def testNumStops_CC3():
    assert r.numStops('C', 'C', 3) == 3

def testNumStops_AC4():
    assert r.findPathWithExactStops('A', 'C', 4) == 3
	
def testShortestRoute_AC():
    assert r.shortestRoute('A', 'C' ) == 9

def testShortestRoute_BB():
    assert r.shortestRoute('B', 'B' ) == 9

def testNumRoutesWithin_CC():
    assert r.numberOfRoutesWithin('C', 'C', 30) == 7