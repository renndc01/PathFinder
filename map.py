class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    #creates a list of the wall locations for the new Map
    #each item in the walls list is a tuple where the location tuple represents the index in the original array
    def createWalls(self, originalMaze):
        for i in range(0, self.width):
            for k in range(0, self.height):
                if(originalMaze[i][k] == 1):
                    self.walls.append((i, k))

    #returns the location in which the pegi guy starts in the original maze
    #the item in which is returned will be a tuple of the index where the pegi starts
    def getStartLocation(self, originalMaze):
        for i in range(0, self.width):
            for k in range(0, self.height):
                if(originalMaze[i][k] == 2):
                    return (i, k)
        return None

    #returns a list of the locations in which a goal item is found in the original maze
    #the list returned will be of tuples where each tuple is an index location where the goal item is located
    def getGoalLocations(self, originalMaze):
        goalLocations = []
        for i in range(0, self.width):
            for k in range(0, self.height):
                if(originalMaze[i][k] == 3):
                    goalLocations.append((i, k))
        return goalLocations

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        if (x + y) % 2 == 0:
            results.reverse()  # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results
