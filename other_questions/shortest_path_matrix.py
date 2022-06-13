"""
Find the shortest path in matrix of nXm where all units are zeros except
1->start
2->end
3->block
"""

paths = []


def startToEnd(matrix):
    if not matrix:
        return "No path available for empty matrix."


grid = [[1, 0, 0],
        [0, 0, 2]]

print(startToEnd(grid))
