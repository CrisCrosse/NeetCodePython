from typing import List


class Position:
    def __init__(self, x: int, y: int):
        self.x = x  # the first index into board selects the row or the y axis
        self.y = y  # the second index selects the column or the x index

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"


class MySolution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def getAdjacentPositions(position: Position) -> List[Position]:
            print(f"getting adjacent positions of {position}")
            # start on right and go clockwise
            # adding one to y index (first index) moves down
            # adding one to x index (second) behaves normally and moves right
            res = []
            offset_x, offset_y = 1, 0
            for i in range(4):
                if i == 1:
                    offset_x -= 1
                    offset_y += 1
                elif i == 2:
                    offset_x -= 1
                    offset_y -= 1
                elif i == 3:
                    offset_x += 1
                    offset_y -= 1
                new_position = Position(position.x + offset_x, position.y + offset_y)

                if new_position.y >= len(board) or new_position.y < 0:
                    continue
                if new_position.x >= len(board[0]) or new_position.x < 0:
                    continue
                print(f"adjacent position passed check with co-ords: {new_position}")
                res.append(new_position)
            return res

        def nextLetterIsAdjacent(position: Position, remaining_word: str,
                                 used_positions_this_run: List[Position]) -> bool:
            print(
                f"at position {position}, with remaining word: {remaining_word} and used positions {", ".join(map(str, used_positions_this_run))}")

            if not len(remaining_word):
                # if we have iterated to the end of the word
                return True

            next_letter = remaining_word[0]
            adjacent_positions = getAdjacentPositions(position)

            for adjacent_position in adjacent_positions:
                adjacent_letter = board[adjacent_position.y][adjacent_position.x]
                if adjacent_letter == next_letter and adjacent_position not in used_positions_this_run:
                    used_positions_this_run.append(adjacent_position)
                    if nextLetterIsAdjacent(adjacent_position, remaining_word[1:], used_positions_this_run):
                        return True
                    used_positions_this_run.pop()
            return False

        first_letter = word[0]

        for y, row in enumerate(board):
            for x, letter in enumerate(row):
                if letter == first_letter:
                    start_position = Position(x, y)
                    if nextLetterIsAdjacent(start_position, word[1:], [start_position]):
                        return True
        return False

class BacktrackingOfficialSolution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (min(r, c) < 0 or
                    r >= ROWS or c >= COLS or
                    word[i] != board[r][c] or
                    (r, c) in path):
                return False

            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
# This is fewer lines of code but harder to read, essentially the same solution as I came up with

# Time complexity: O(m * 4^n)
# Space complexity: O(n)

class NotUsingExtraSpaceForVisited:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False

            # this char marks the square as visited
            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            # restore current position to original value as finished depth first search 
            board[r][c] = word[i]
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False