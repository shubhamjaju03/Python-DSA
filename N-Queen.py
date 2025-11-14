def solveNQueens(n):
    solutions = [] 
  
    def place_queen(row, queens, columns, diagonals1, diagonals2):
        if row == n:
            board = []
            for q in queens:
                row_str = ['.'] * n
                row_str[q] = 'Q'
                board.append(''.join(row_str))
            solutions.append(board)
            return

        for col in range(n):
            if col in columns or (row - col) in diagonals1 or (row + col) in diagonals2:
                continue

            queens.append(col)
            columns.add(col)
            diagonals1.add(row - col)
            diagonals2.add(row + col)


            place_queen(row + 1, queens, columns, diagonals1, diagonals2)

            queens.pop()
            columns.remove(col)
            diagonals1.remove(row - col)
            diagonals2.remove(row + col)

    place_queen(0, [], set(), set(), set())
    return solutions
  
for solution in solveNQueens(4):
    for row in solution:
        print(row)
    print()
