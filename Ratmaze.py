def maze(n, m):
    result = []

    def solve(row, column, path):
        path.append((row, column))
        if row == n - 1 and column == m - 1:
            result.append(list(path))
            path.pop()
            return
        if row + 1 < n:
            solve(row + 1, column, path)
        if column + 1 < m:
            solve(row, column + 1, path)
        path.pop()
    solve(0, 0, [])
    return result
    
n_rows = int(input("How many rows? "))
m_cols = int(input("How many columns? "))
paths = maze(n_rows, m_cols)

print("Here are the possible paths:")
for path in paths:
    print(path)
