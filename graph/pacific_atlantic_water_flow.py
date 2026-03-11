from collections import deque
from typing import List


class NonPassableTimeSolution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pacific = atlantic = False

        def dfs(r, c, prevVal):
            nonlocal pacific, atlantic
            # top or left of grid = pacific
            if r < 0 or c < 0:
                pacific = True
                return
            # bottom or right of grid = atlantic
            if r >= ROWS or c >= COLS:
                atlantic = True
                return
            # if water will not flow to next island (cannot go uphill) return
            if heights[r][c] > prevVal:
                return

            # get value to restore after we mark as visited
            tmp = heights[r][c]
            # set current to max height "visited" so we do not infinite loop while exploring
            heights[r][c] = float('inf')
            # explore each direction and if we ever set both bools to true exit dfs
            for dx, dy in directions:
                dfs(r + dx, c + dy, tmp)
                if pacific and atlantic:
                    break
            heights[r][c] = tmp

        res = []
        # for each square do a full DFS of every reachable grid
        for r in range(ROWS):
            for c in range(COLS):
                pacific = False
                atlantic = False
                dfs(r, c, float('inf'))
                if pacific and atlantic:
                    res.append([r, c])
        return res

# Time complexity: O(m*n*4^(m*n))
# Space complexity: O(m*n)

class DFSFromOceanCells:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        # two solution sets of co-ords reachable via ocean
        # reverse flow direction so height needs to be greater than prev
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            # if out of bounds, already visited or down from previous, cannot visit and exit dfs
            if ((r, c) in visit or
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                heights[r][c] < prevHeight
            ):
                return
            # explore all visitable cells
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # top and bottom ocean cells
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # left and right ocean cells
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res

# Time complexity: O(m*n)
# Space complexity: O(m*n)

class BFSFromOceanCells:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        def bfs(ocean_source, water_can_flow_from_ocean_bool_grid):
            q = deque(ocean_source)
            while q:
                # get reachable tile
                r, c = q.popleft()
                # change
                water_can_flow_from_ocean_bool_grid[r][c] = True
                # for each direction if valid tile and has greater height than current then it is reachable so add to q
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        not water_can_flow_from_ocean_bool_grid[nr][nc] and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        q.append((nr, nc))

        pacific = []
        atlantic = []
        # append top and bottom cells to corresponding oceans
        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))

        # append left and right cells to corresponding oceans
        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))


        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res