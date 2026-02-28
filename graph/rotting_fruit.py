from collections import deque
from typing import List


class MyInitialAttempt:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        max_row = len(grid)
        max_column = len(grid[0])
        q = deque()
        fresh_fruit_count = 0
        visited = [False for index in range(max_row * max_column)]

        # get fresh fruit count so we can tell when all fruit has rotted
        for row_index, row in enumerate(grid):
            for column_index, cell in enumerate(row):
                if cell == 1:
                    fresh_fruit_count += 1
                elif cell == 2:
                    # get all starting points for multipoint breadth first search - all rotting fruit
                    q.append((row_index, column_index))

        # if all fruit already rotten then 0 minutes needed to rot
        if fresh_fruit_count == 0:
            return 0


        def addToQIfFreshFruit(row_index, column_index, fresh_fruit_count):
            if row_index < 0 or row_index >= max_row:
                return fresh_fruit_count
            if column_index < 0 or column_index >= max_column:
                return fresh_fruit_count
            cell = grid[row_index][column_index]
            index_in_visited = (row_index * max_column) + column_index

            # prevent adding the same rotten fruit to the queue multiple times and doing duplicated work, and throwing
            # off the count
            if cell == 1 and not visited[index_in_visited]:
                fresh_fruit_count -= 1
                q.append((row_index, column_index))
                visited[index_in_visited] = True
            return fresh_fruit_count

        minute = 0
        while q:
            # for each level in the breadth first search increase minutes by one,
            # we are searching for adjacent fresh fruit
            for _ in range(len(q)):
                rotting_fruit = q.popleft()
                r = rotting_fruit[0]
                c = rotting_fruit[1]
                print(f"rotting fruit {rotting_fruit}, row {r}, column {c}")
                fresh_fruit_count = addToQIfFreshFruit(r + 1, c, fresh_fruit_count)
                fresh_fruit_count = addToQIfFreshFruit(r, c + 1, fresh_fruit_count)
                fresh_fruit_count = addToQIfFreshFruit(r - 1, c, fresh_fruit_count)
                fresh_fruit_count = addToQIfFreshFruit(r, c - 1, fresh_fruit_count)
            minute += 1
            if fresh_fruit_count == 0:
                return minute
        return -1

class BFSSolution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0

        # same approach as I did count the fresh fruit and using the rotten fruit as the launching points
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid))
                            and col in range(len(grid[0]))
                            and grid[row][col] == 1
                    ):
                        # mutating the grid in place
                        # not using a visited check just using the in place mutation
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

