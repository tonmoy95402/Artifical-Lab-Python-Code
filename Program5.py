def graph_coloring(graph, m, color, node):
    # If all nodes are colored
    if node == len(graph):
        return True

    for c in range(1, m + 1):
        ok = True

        # Check adjacent nodes
        for neighbor in graph[node]:
            if color[neighbor] == c:
                ok = False
                break

        if ok:
            color[node] = c

            if graph_coloring(graph, m, color, node + 1):
                return True

            color[node] = 0  # backtrack

    return False


# -------- MAIN --------
n, m, k = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

color = [0] * n

if graph_coloring(graph, k, color, 0):
    print(f"Coloring Possible with {k} Colors")
    print("Color Assignment:", color)
else:
    print(f"Coloring Not Possible with {k} Colors")