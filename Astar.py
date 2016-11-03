def Astar(start, goal):
    closedSet = {}
    openSet = {start}
    # cameFrom = the empty map

    # gScore = map with default value of Infinity
    gScore[start] = 0
    # fScore = map with default value of Infinity
    fScore[start] =heuristic_cost_estimate(start, goal)

    while openSet is not empty:
        # current = node in openSet having lowest fScore value
        if (current == goal):
            return reconstruct_path(cameFrom, current)
        
        openSet.remove(current)
        closedSet.add(current)
        for neighbor in current.neighbors:
            if neighbor in closedSet:
                continue
            tentitive_gScore = gScore[current] + dist_between(current, neighbor)
            if neighbor not in openSet:
                openSet.add(neighbor)
            elif tentative_gScore >= gScore[neighbor]:
                continue
            cameFrom[neighbor] = current
            gScore[neighbor] = tentative_gScore
            fScore[neighbor] = gScore[neighbor] + heuristic_cost_estimate(neighbor, goal)
    return null

def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom.keys:
        current = cameFrom[current]
        totalPath.append(current)
    return totalPath