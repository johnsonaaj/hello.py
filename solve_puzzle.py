def solve_puzzle(board, start, visited=None):
    if visited is None:
        visited = set()

    if start == len(board) - 1:
        return True

    visited.add(start)

    for move in [board[start], -board[start]]:
        next_pos = (start + move) % len(board)

        if next_pos in visited:
            continue

        if solve_puzzle(board, next_pos, visited):
            return True

    return False