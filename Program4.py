def iddfs_maze_solver(grid, start, target, max_depth_limit):
    rows = len(grid)
    cols = len(grid[0])

    def dls(current, target, depth, path):
        """Depth-Limited Search (DLS) helper function."""
        if current == target:
            return path
        if depth <= 0:
            return None

        r, c = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            # Check boundaries, if it's a path (1), and not already in current path
            if (0 <= nr < rows and 0 <= nc < cols and
                    grid[nr][nc] == 1 and (nr, nc) not in path):

                path.append((nr, nc))
                result = dls((nr, nc), target, depth - 1, path)
                if result:
                    return result
                path.pop()  # Backtracking
        return None


    for depth in range(max_depth_limit + 1):
        found_path = dls(start, target, depth, [start])
        if found_path:
            return depth, found_path

    return None, None


# --- Case Execution ---

# Case #1
maze1 = [
    [1, 0, 1, 0],
    [1, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 1, 0, 1]
]
s1, t1 = (0, 0), (2, 3)
d1, p1 = iddfs_maze_solver(maze1, s1, t1, 10)
print(f"Case #1: Path found at depth {d1} using IDDFS\nTraversal Order: {p1}\n")

# Case #2 (0s are paths, 1s are walls in this specific grid)
maze2 = [
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1]
]
# In Case 2, (0,0) to (2,2) is blocked by a wall of 0s at column 1.
s2, t2 = (0, 0), (2, 2)
d2, p2 = iddfs_maze_solver(maze2, s2, t2, 6)

if p2:
    print(f"Case #2: Path found at depth {d2}")
else:
    print(f"Case #2: Path not found at max depth 6 using IDDFS")