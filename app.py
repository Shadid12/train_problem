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

print(r.distanceBetween(['A','D']))

print(r.distanceBetween(['A','D']))

print(r.distanceBetween(['A','D','C']))

print(r.distanceBetween(['A','E','B', 'C', 'D']))

print(r.distanceBetween(['A','E','D']))

print(r.numStops('C', 'C', 3))

print(r.findPathWithExactStops('A', 'C', 4))

print(r.shortestRoute('A', 'C' ))

print(r.shortestRoute('B', 'B' ))

print(r.numberOfRoutesWithin('C', 'C', 30))




