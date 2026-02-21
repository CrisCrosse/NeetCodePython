from collections import deque
from typing import List


class Coord:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"y: {self.y}, x: {self.x}"

    def __eq__(self, other):
        if isinstance(other, Coord):
            return (self.x, self.y) == (other.x, other.y)
        return False

    def __hash__(self):
        return hash((self.x, self.y))


class MySolution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # keep track of current number of islands, all land co ords for O(1) lookups of land, map of island number to co-ords
        # to make more effecient I could also map each co-ord to it's island?
        count = 0
        islands = {} # island number to list of co-ords, make the co-ords a set for O(1) lookups instead of O(n)
        island_coords = set()

        for y, row in enumerate(grid):
            for x, square in enumerate(row):
                # do nothing for water
                if square == "0":
                    continue

                current = Coord(x, y)
                island_coords.add(current)
                square_above = Coord(x, y - 1)
                square_left = Coord(x - 1, y)


                if square_above in island_coords and square_left in island_coords:
                    # find if islands already linked,
                    for island_number in range(1, count + 1):
                        co_ords_for_this_island = islands[island_number]
                        if square_left in co_ords_for_this_island:
                            left_island = island_number
                        if square_above in co_ords_for_this_island:
                            above_island = island_number

                    # if linked just add this coord
                    if above_island == left_island:
                        co_ords_for_this_island = islands[above_island]
                        all_co_ords = co_ords_for_this_island + [current]
                        islands[above_island] = all_co_ords
                    # if not merge co ords, decrease count and remove from dict
                    else:
                        left_co_ords = islands[left_island]
                        above_co_ords = islands[above_island]
                        left_is_higher_numbered_island = left_island > above_island
                        island_to_delete = left_island if left_is_higher_numbered_island else above_island
                        island_to_keep = above_island if left_is_higher_numbered_island else left_island

                        del islands[island_to_delete]
                        all_co_ords = left_co_ords + above_co_ords + [current]
                        islands[island_to_keep] = all_co_ords

                        # if not deleting at end of sequence, shift all island indexes after deletion down one
                        # so we keep a continuous ascending set of island numbers
                        for island_number in range(island_to_delete + 1, count + 1):
                            tmp = islands[island_number]
                            del islands[island_number]
                            islands[island_number - 1] = tmp
                        count -= 1
                    continue

                # add current co ord to existing island
                if square_left in island_coords:
                    for island_number in range(1, count + 1):
                        co_ords_for_this_island = islands[island_number]
                        if square_left in co_ords_for_this_island:
                            co_ords_for_this_island.append(current)
                            islands[island_number] = co_ords_for_this_island
                            break
                    continue
                if square_above in island_coords:
                    for island_number in range(1, count + 1):
                        co_ords_for_this_island = islands[island_number]
                        if square_above in co_ords_for_this_island:
                            co_ords_for_this_island.append(current)
                            islands[island_number] = co_ords_for_this_island
                            break
                    continue

                # new island
                count += 1
                if count in islands:
                    print(f"something has gone seriously wrong, trying to add an existing island count to dict")
                    print(f"x: {x}, y: {y}")
                    print(f"attempting to add: {count}")
                    print(f"islands: {islands.keys()}")
                islands[count] = [current]
        return count

class DFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or
                    c >= COLS or grid[r][c] == "0"
            ):
                return

            # mark any visited island grids as 0 so we do not double count
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands

# quite elegant

# Time complexity: O(m * n) m is the number of rows and n is the number of columns
# Space complexity: O(m∗n)

class BFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or
                            nc >= COLS or grid[nr][nc] == "0"
                    ):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands

class DSU:
    def __init__(self, n):
        self.Parent = list(range(n + 1))

        # size at each index of all islands attached to it
        self.Size = [1] * (n + 1)

    # we pass in indexes here
    def find(self, node):
        # if this nodes parent node is not itself
        if self.Parent[node] != node:
            # set parent as find of current value (parent list is not initialised so is null?
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        # if parents equal, they are already unioned so do nothing
        if pu == pv:
            return False
        # if u has greater current size than v
        if self.Size[pu] >= self.Size[pv]:
            # set pu size to include pv
            self.Size[pu] += self.Size[pv]
            # make pu parent of pv
            self.Parent[pv] = pu
        else:
            # set pv size to include pu
            self.Size[pv] += self.Size[pu]
            # set pv as parent of u
            self.Parent[pu] = pv
        # we did union the two
        return True

class DisJointSetUnion:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dsu = DSU(ROWS * COLS)

        def index(r, c):
            return r * COLS + c

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    islands += 1
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (nr < 0 or nc < 0 or nr >= ROWS or
                                nc >= COLS or grid[nr][nc] == "0"
                        ):
                            continue

                        if dsu.union(index(r, c), index(nr, nc)):
                            islands -= 1

        return islands