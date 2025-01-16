from collections import deque

def ford_fulkerson(graph, source, sink):
    flow = 0
    parent = [-1] * len(graph)

    while bfs(graph, source, sink, parent):
        path_flow = float('Inf')
        s = sink

        # Find the minimum flow in the found path
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        # Update residual capacities and reverse edges
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

        flow += path_flow

    return flow

def bfs(graph, source, sink, parent):
    visited = [False] * len(graph)
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()

        for i, val in enumerate(graph[u]):
            if not visited[i] and val > 0:  # If not visited and there's remaining capacity
                queue.append(i)
                visited[i] = True
                parent[i] = u

    return visited[sink]