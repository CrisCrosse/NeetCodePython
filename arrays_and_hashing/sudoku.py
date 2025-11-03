from typing import List


class Solution:
    # the example used sets, probably cleaner that way without dictionary access it is just if element in seen return False
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each row
        for row in board:
            frequency_dict = {}
            for element in row:
                if element == ".":
                    continue
                frequency_dict[element] = frequency_dict.get(element, 0) + 1
                if frequency_dict[element] > 1:
                    return False
        # check each column
        for column_number in range(9):
            frequency_dict = {}
            for row_number in range(9):
                element = board[row_number][column_number]
                if element == ".":
                    continue
                frequency_dict[element] = frequency_dict.get(element, 0) + 1
                if frequency_dict[element] > 1:
                    return False

        # check all 9 boxes, top left to top right, middle left to middle right then bottom left to bottom right

        for vertical_offset in range(0, 9, 3):
            for horizontal_offset in range(0, 9, 3):
                frequency_dict = {}
                print(f"looking at 9 square box at co-ords: {horizontal_offset}, {vertical_offset}")
                for row_number in range(3):
                    for column_number in range(3):
                        element = board[vertical_offset + row_number][horizontal_offset + column_number]
                        print(
                            f"examining element {element} at index[{vertical_offset + row_number}][{horizontal_offset + column_number}]")
                        if element == ".":
                            continue
                        frequency_dict[element] = frequency_dict.get(element, 0) + 1
                        if frequency_dict[element] > 1:
                            return False

        return True
    # This solution has O(3 * n) time complexity or O(n) because we iterate over each element 3 times
    # It also has O(3 * n) space complexity as in the worst case we create 3 dicts of length n, although only 1 at a time

class Bitmask:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        # simple case [ 3, 2, 3] needs to return false

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                # why do we minus 1 here?, to get values 0 - 8?
                # 0000, 0001, 0010, 0011, 0100, 0101, 0110, 0111, 1000
                # the solution works without minusing 1 here
                val = int(board[r][c]) - 1
                # val:3 1000 & 0000 --> 0000,
                # val:2 0100 & 1000 --> 0000,
                # val:3 1000 & 1100 --> 0100 --> False
                if (1 << val) & rows[r]:
                    return False
                if (1 << val) & cols[c]:
                    return False
                if (1 << val) & squares[(r // 3) * 3 + (c // 3)]:
                    return False

                #  0000 | 1000 --> 1000,
                # 1000 | 0100 --> 1100
                # this is effectively adding a 1 at the index moving left of the value
                rows[r] |= (1 << val)
                cols[c] |= (1 << val)
                squares[(r // 3) * 3 + (c // 3)] |= (1 << val)

        return True