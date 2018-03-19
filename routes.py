import sys

class Routes:

    def __init__(self, routesTable={}):
        # the routesTable is our hash map DT
        self.routesTable = routesTable
    
    def distanceBetween(self, cities=[]):
        
        """
        Calculates distance of the route
        Args:
            cities (str[]): The array of cities

        Returns:
            int: calclated distance
        """

        distance = 0 
        '''
        for every cities we will be looking at the adjacent route and 
        adding the weight of route to total distance
        '''
        for i in range(len(cities)):
            root_node = cities[i]
            if i + 1 < len(cities):
                next_node = cities[i+1]
                if next_node in self.routesTable[root_node]:
                    distance = distance + self.routesTable[root_node][next_node]
                else: 
                    return "There is no route"
        return distance
    
    def numStops(self, start, end, maxStops):
        """
        Wrapper function to calculate the number of stops
        Args:
            start    (str):    Starting city
            end      (str):    Destination city
            maxStops (int):    number of maximum stops allows

        Returns:
            int: calclated number of routes
        """
        return self.findRoutes(start, end, 0, maxStops)
    
    def findRoutes(self, start, end, depth, maxStops):
        """
        Recursive function to calculate the number of stops
        Args:
            start    (str):    Starting city
            end      (str):    Destination city
            maxStops (int):    number of maximum stops allows
            depth    (int):    current depth of recursion

        Returns:
            int: calclated number of routes
        """

        visited =[]
        routes = 0
        # Check if start and end nodes exists in route table
        if start in self.routesTable and end in self.routesTable:
            depth = depth + 1
            if depth > maxStops:  # Check if depth level is within limit
                return 0
            visited.append(start) # mark start as visited

            for adj in self.routesTable[start]:
                '''
                If destination matches, we increment route
				count, then continue to next node at same depth
				'''
                if adj == end:
                    routes = routes + 1
                
                '''
                If destination does not match, and
				destination node has not yet been visited,
				we recursively traverse destination node
				'''
                if adj not in visited and adj != end:
                    depth = depth - 1
                    routes += self.findRoutes(adj, end, depth, maxStops)
        else:
            return "No Such route"
        
        # unmark the start node before leaving recursive func
        if start in visited:
            visited.remove(start)
        return routes
    

    def shortestRoute(self, start, end):
        """
        Wrapper function to calculate the shortest route
        Args:
            start    (str):    Starting city
            end      (str):    Destination city

        Returns:
            int: calclated weight of the shortest route
        """
        return self.findShortestRoute(start, end, 0, 0)

    def findShortestRoute(self, start, end , weight, shortestRoute, visited=[]):
        """
        Recursive function to calculate the shortest route
        Args:
            start           (str):      Starting city
            end             (str):      Destination city
            weight          (weight):   weight of the route
            shortestRoute   (int):      shortest path so far
            visited         (str[]):    array of visited nodes

        Returns:
            int: calclated weight of the shortest route
        """

        # Check if start and end nodes exists in route table
        if start in self.routesTable and end in self.routesTable:
            visited.append(start) # mark start to visited

            for adj in self.routesTable[start]:
                if(adj == end or adj not in visited):
                    weight += self.routesTable[start][adj]
                    
                '''
                If destination matches, we compare
                weight of this route to shortest route
                so far, and make appropriate switch
                '''

                if adj == end:
                    if shortestRoute == 0 or weight < shortestRoute:
                        shortestRoute = weight
                    visited.remove(start)
                    return shortestRoute
                '''
                If destination does not match, and
				destination node has not yet been visited,
				we recursively traverse destination node
                '''
                if adj not in visited:
                    shortestRoute = self.findShortestRoute(adj, end, weight, shortestRoute, visited)
                    weight -= self.routesTable[start][adj]
        
        else:
            return "No such route exists"

        if start in visited:
            visited.remove(start)
        
        return shortestRoute

    def numberOfRoutesWithin(self, start, end, maxDistance):
        """
        Wrapper function to calculate the number of routes within a given limit
        Args:
            start           (str):      Starting city
            end             (str):      Destination city
            maxDistance     (int):      Maximum distance/limit 

        Returns:
            int: number of routes
        """
        return self.findNumberOfRoutesWithin(start, end, 0, maxDistance)
    
    def findNumberOfRoutesWithin(self, start, end , weight, maxDistance, routes=0):
        """
        Recursive function to calculate the number of routes within a given limit
        Args:
            start           (str):      Starting city
            end             (str):      Destination city
            weight:         (int):      Weight of the route
            maxDistance     (int):      Maximum distance/limit
            routes:         (int):      Current routes in the recursion

        Returns:
            int: number of routes
        """
        # check if start and end node exists in the graph
        if start in self.routesTable and end in self.routesTable:
            '''
            If start node exists then traverse all possible
			routes and for each, check if it is destination
            '''
            for adj in self.routesTable[start]:
                weight += self.routesTable[start][adj]
                '''
                If distance is under max, keep traversing
				even if match is found until distance is > max
                '''
                if weight <= maxDistance:
                    if adj == end:
                        routes = routes + 1
                        routes += self.findNumberOfRoutesWithin(adj, end, weight, maxDistance)
                    else:
                        routes += self.findNumberOfRoutesWithin(adj, end, weight, maxDistance)
                        weight -= self.routesTable[start][adj] # Decrement weight as we backtrack
                else:
                    weight -= self.routesTable[start][adj]
        else:
            print("No such route")
        
        return routes

    def findPathWithExactStops(self, start, finish, exact):
        """
        Wrapper function to calculate the path with exact number of stops
        Args:
            start           (str):      Starting city
            end             (str):      Destination city
            maxDistance     (int):      exact number of stops

        Returns:
            int: number of routes
        """
        count = 0
        visited = []
        path = []

        path.append(start)
        visited.append(start)

        for adjacent_node in self.routesTable[start]:
            if adjacent_node not in visited:
                count = self.printAllPathsUtil(adjacent_node, finish, visited, path, exact, count)
        
        return count

    
    # util methods for cycle detection
    def printAllPathsUtil(self, start, finish, visited, path, exact, count):
        """
        Recursive function to calculate the number of routes within a given limit
        Args:
            start           (str):        Starting city
            end             (str):        Destination city
            visited         (str[]):      Maximum distance/limit 
            path            (str[]):      path so far
            exact           (int):        limit
            count           (int):        number of paths found so far 

        Returns:
            int: count 
        """
        visited.append(start)
        path.append(start)

        if start == finish:
            if len(path) < exact:
                count = self.findCycle(finish, path, exact, count)
            
            if len(path) == exact + 1:
                print(path)
                count = count + 1
        
        else:
            for adjacent_node in self.routesTable[start]:
                if adjacent_node not in visited:
                    count = self.printAllPathsUtil(adjacent_node, finish, visited, path, exact, count)
        
        path.pop()
        visited.remove(start)

        return count


    def findCycle(self, start, path, exact, count):
        """
        Wrapper function to detect cycle in the graph
        Args:
            start           (str):        Starting city
            end             (str):        Destination city
            path            (str[]):      path so far
            exact           (int):        limit
            count           (int):        number of paths found so far 

        Returns:
            int: count 
        """
        visited = []

        for adj_node in self.routesTable[start]:
            if adj_node not in visited:
                count = self.findCycleUtil(adj_node, start, path, visited, exact, count)
        return count
    

    def findCycleUtil(self, start, end, path, visited, exact, count):
        """
        recursive function to detect circular path in the graph
        Args:
            start           (str):        Starting city
            end             (str):        Destination city
            path            (str[]):      path so far
            visited         (str[]):      visited nodes so far 
            exact           (int):        limit
            count           (int):        number of paths found so far 

        Returns:
            int: count 
        """
        visited.append(start)
        path.append(start)

        if start == end:
            if len(path) == exact + 1:
                count = count + 1
                print(path)
        else:
            for adj_node in self.routesTable[start]:
                if adj_node not in visited:
                   count = self.findCycleUtil(adj_node, end, path, visited, exact, count)

        path.pop()
        visited.remove(start) 

        return count