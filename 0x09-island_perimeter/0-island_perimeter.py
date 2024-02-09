#!/usr/bin/python3
"""
Calculating the island perimeter
"""


def island_perimeter(grid):
    """
    Return perimeter of island
    """
    if type(grid) is not list:
        return 0
    perimeter = 0
    i = len(grid)
    for k, row in enumerate(grid):
        j = len(row)
        for m, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                k == 0 or (len(grid[k - 1]) > m and grid[k - 1][m] == 0),
                m == j - 1 or (j > m + 1 and row[m + 1] == 0),
                k == i - 1 or (len(grid[k + 1]) > m and grid[k + 1][m] == 0),
                m == 0 or row[m - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
