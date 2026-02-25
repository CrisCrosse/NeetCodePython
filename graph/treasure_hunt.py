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
            print(f"looking at row index {row} and column index {column}")
            if row < 0 or row == max_row:
                return 2147483647
            if column < 0 or column == max_column:
                return 2147483647

            square = grid[row][column]
            print(f"square value is {square}")
            if square == 0:
                return 0
            if square == -1:
                return 2147483647

            if square == 2147483647:
                print(f"traversing other squares to find min distance to treasure")
                # entering infinite loop because I traverse back to the same square I just visited
                minimum_adjacent_distance_to_treasure = min(dfs(row + 1, column), dfs(row, column + 1),
                                                            dfs(row - 1, column), dfs(row, column - 1))
                distance_to_treasure = minimum_adjacent_distance_to_treasure + 1
                # grid[row][column] = distance_to_treasure
                print(f"grid: {grid}")
                return distance_to_treasure

            return square

        for row_index, row in enumerate(grid):
            for column_index, square in enumerate(row):
                visited = set()
                if square == 2147483647:
                    grid[row_index][column_index] = dfs(row_index, column_index)

