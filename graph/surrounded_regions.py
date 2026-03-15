from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        max_row = len(board)
        max_column = len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= max_row or c >= max_column:
                return
            region = board[r][c]
            if region != "O":
                return

            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        # start at each border cell,
        # if cell is O then mark as temp -> T
        # # explore each linked O cell from borders
        for index in range(max_row):
            dfs(index, 0)
            dfs(index, max_column - 1)

        for index in range(max_column):
            dfs(0, index)
            dfs(max_row - 1, index)

        # Loop through whole set of squares and mark any Os as X and any Ts as Os
        # allows in place memory useage by marking as T in place
        for row_index, row in enumerate(board):
            for column_index, region in enumerate(row):
                if region == "O":
                    board[row_index][column_index] = "X"
                elif region == "T":
                    board[row_index][column_index] = "O"

# Time & Space Complexity
# Time complexity: O(m*n)
# Space complexity: O(m*n)



