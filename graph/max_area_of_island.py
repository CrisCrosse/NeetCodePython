from collections import deque
from typing import List


class MySolutionDepthFirstSearch:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        max_row = len(grid)
        max_column = len(grid[0])

        def dfs(row, column):
            if row < 0 or row == max_row:
                return 0
            if column < 0 or column == max_column:
                return 0

            print(f"dfs for row {row}, column {column} with value {grid[row][column]}")

            square = grid[row][column]
            if square == 1:
                # overwrite explored squares so we only dfs every island once
                grid[row][column] = "0"
                current_area = 1 + dfs(row + 1, column) + dfs(row, column + 1) + dfs(row - 1, column) + dfs(row,
                                                                                                            column - 1)
                print(f"finished dfs at this level, returning area {current_area}")
                return current_area
            else:
                return 0

        for row_index, row in enumerate(grid):
            for column_index, column in enumerate(row):
                print(f"checking area at {row_index}, {column_index}")
                if grid[row_index][column_index] == 1:
                    this_islands_area = dfs(row_index, column_index)
                    print(f"area of island at {row_index}, {column_index} was {this_islands_area}")
                    max_area = max(max_area, this_islands_area)

        return max_area

# This solutions time complexity should be O(n * 4^n) where n is the number of 1 or island squares, because we iterate over every square and if an island square we then do a dfs search with 4 branches
# Space complexity is the same due to recursion having a lot of open variables equal to the recursion depth

# apparently it is:
# Time complexity: O(m * n)
# m * n because we should only visit each cell once (not quite true as we will go back to visited cells but return out of the dfs)
# Space complexity: O(m∗n)

class DepthFirstSearch:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # this one uses a visit to stop going back to cells already visited, slightly better than my setting to 0 because
        visit = set()

        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or
                    c == COLS or grid[r][c] == 0 or
                    (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            return (1 + dfs(r + 1, c) +
                    dfs(r - 1, c) +
                    dfs(r, c + 1) +
                    dfs(r, c - 1))

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area




class  BreadthFirstSearch:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        area = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            res = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or
                        nc >= COLS or grid[nr][nc] == 0
                    ):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    res += 1
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))

        return area

    # Same time and space complexity





# still need to see how this works
class DSU:
    def __init__(self, n):
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.Size[pu] >= self.Size[pv]:
            self.Size[pu] += self.Size[pv]
            self.Parent[pv] = pu
        else:
            self.Size[pv] += self.Size[pu]
            self.Parent[pu] = pv
        return True

    def getSize(self, node):
        par = self.find(node)
        return self.Size[par]

class DisjointSetUnion:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dsu = DSU(ROWS * COLS)

        def index(r, c):
            return r * COLS + c

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        area = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (nr < 0 or nc < 0 or nr >= ROWS or
                                nc >= COLS or grid[nr][nc] == 0
                        ):
                            continue

                        dsu.union(index(r, c), index(nr, nc))

                    area = max(area, dsu.getSize(index(r, c)))

        return area
# Same time and space complexity