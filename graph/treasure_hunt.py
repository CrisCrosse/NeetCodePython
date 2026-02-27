from collections import deque
from typing import List


class PartialSolution7OutOf15TestsPass:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        max_row = len(grid)
        max_column = len(grid[0])

        def dfs(row, column):
            coord = (row, column)
            if coord in visited:
                return 2147483647
            visited.add(coord)
            # print(f"looking at row index {row} and column index {column}")
            if row < 0 or row == max_row:
                return 2147483647
            if column < 0 or column == max_column:
                return 2147483647

            square = grid[row][column]
            # print(f"square value is {square}")
            if square == 0:
                return 0
            if square == -1:
                return 2147483647

            if square == 2147483647:
                # print(f"traversing other squares to find min distance to treasure")
                # entering infinite loop because I traverse back to the same square I just visited
                row_down = dfs(row + 1, column)
                column_right = dfs(row, column + 1)
                row_above = dfs(row - 1, column)
                column_left = dfs(row, column - 1)
                if row == 0 and column == 0:
                    print(
                        f"finished recursion at base square, row_down {row_down}, column_right {column_right}, row_above {row_above}, column_left {column_left}")
                minimum_adjacent_distance_to_treasure = min(row_down, column_right, row_above, column_left)
                distance_to_treasure = minimum_adjacent_distance_to_treasure + 1
                # grid[row][column] = distance_to_treasure
                # print(f"grid: {grid}")
                visited.remove(coord)
                return distance_to_treasure

            return square

        for row_index, row in enumerate(grid):
            for column_index, square in enumerate(row):
                visited = set()
                if square == 2147483647:
                    grid[row_index][column_index] = dfs(row_index, column_index)

class DFSSolution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647
        visit = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(r, c):
            print(f"checking row: {r}, column {c}")
            if r == 0 and c == 1:
                print(f"at treasure index, visited: {visit[r][c]}, square: {grid[r][c]}")
            if (r < 0 or c < 0 or r >= ROWS or
                    c >= COLS or grid[r][c] == -1 or
                    visit[r][c]):
                return INF
            if grid[r][c] == 0:
                return 0

            visit[r][c] = True
            res = INF
            for dx, dy in directions:
                res = min(res, 1 + dfs(r + dx, c + dy))
            visit[r][c] = False
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = dfs(r, c)

# actually not a solution due to time limit exceeded

class NotPassingForTime:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        max_row = len(grid)
        max_column = len(grid[0])
        INF = 2147483647
        visited = [[False for _ in range(max_column)] for _ in range(max_row)]

        # Time limite exceeded despite being very similar to given solution which passes
        def dfs(row, column):
            coord = (row, column)
            # if row == 0 and column == 1:
            #     print(f"at treasure index, visited: {coord in visited}, on col right {is_on_col_right} visited {visited}")
            if row < 0 or row >= max_row or column < 0 or column >= max_column or visited[row][column]:
                return INF

            square = grid[row][column]

            if square == 0:
                return 0
            if square == -1:
                return INF

            visited[row][column] = True
            coords = [(row + 1, column), (row, column + 1), (row - 1, column), (row, column - 1)]
            res = INF
            for coord in coords:
                res = min(res, 1 + dfs(coord[0], coord[1]))
            # This is the important bit to ensure each level of recursion has it's own view of its previously visited columns,
            # otherwise you get errors where a more circuitous route which is longer to treasure overwrites a more direct route which is just later in recursion depth
            visited[row][column] = False
            return res

        for row_index, row in enumerate(grid):
            for column_index, square in enumerate(row):
                if square == 2147483647:
                    grid[row_index][column_index] = dfs(row_index, column_index)

# Time complexity: O(m*n*4^(m*n))  In the worst case for every grid cell we search the whole grid 4 times over due to branching 4 times at each dfs
# Space complexity: O(m*n*4^(m*n))


class BreadthFirstSearch:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        def bfs(r, c):
            q = deque([(r, c)])
            # each cell has it's own view of visit because we do not reset these within a BFS as we do with DFS
            visit = [[False] * COLS for _ in range(ROWS)]
            visit[r][c] = True
            steps = 0

            while q:
                # why is this needed rather than just popping left?
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if (0 <= nr < ROWS and 0 <= nc < COLS and
                            not visit[nr][nc] and grid[nr][nc] != -1
                        ):
                            visit[nr][nc] = True
                            q.append((nr, nc))
                # needed because at each step outwards we need to increase the number of steps we took
                steps += 1
            return INF

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)

# Time complexity: O((m*n)^2)  m is the number of rows and n is the number of columns,
# for each grid cell in the worst case we search every other grid cell but not as much duplication within a single cell search as we return as soon as we find a treasure
# Space complexity: O(m*n)^2


class MultiSourceBreadthFirstSearch:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()


        def addCell(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == -1
            ):
                # do not add to q if not valid cell in grid
                # do not add to q if already visited by another traversal as we would overwrite it with a greater distance
                # do not add to q if water cell and not traversable
                return
            # otherwise mark this cell as visited and add to q
            visit.add((r, c))
            q.append([r, c])

        # append all treasure cells to q
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            # for cell in the queue
            for i in range(len(q)):
                r, c = q.popleft()
                # set current cell to dist
                grid[r][c] = dist
                # add all adjacent cells to q and mark as visited
                # if a cell is equidistant between two treasure cells the path first due to the order that the direction
                # is in below will set it and the other will ignore, but both will result in the same distance
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1

# Time complexity: O(m*n) We traverse each cell to get the starting treasure points, then via BFS will traverse each cell again
# Space complexity: O(m*n)