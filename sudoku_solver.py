class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [0]*9
        cols = [0]*9
        boxes = [0]*9
        empty = []

        def bit(num):
            return 1 << (num - 1)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    n = int(board[r][c])
                    mask = bit(n)
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[(r//3)*3 + (c//3)] |= mask

        def backtrack(idx=0):
            if idx == len(empty):
                return True
            r, c = empty[idx]
            b = (r//3)*3 + (c//3)
            for num in range(1, 10):
                m = bit(num)
                if (rows[r] & m) or (cols[c] & m) or (boxes[b] & m):
                    continue
                board[r][c] = str(num)
                rows[r] |= m
                cols[c] |= m
                boxes[b] |= m

                if backtrack(idx + 1):
                    return True

                board[r][c] = '.'
                rows[r] &= ~m
                cols[c] &= ~m
                boxes[b] &= ~m
            return False

        backtrack()
