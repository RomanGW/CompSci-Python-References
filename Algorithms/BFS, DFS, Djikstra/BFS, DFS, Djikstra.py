from collections import deque

def bfs(graph, start):
    """
    Traverse the graph using Breadth First Search starting from the given node.
    Return the order in which the nodes are visited.
    """
    queue = deque([start])
    visited_nodes = []
    
    while queue:
        # Pop first node from queue.
        node = queue.popleft()

        if node not in visited_nodes:
            # Add node to visited nodes.
            visited_nodes.append(node)
            # Add neighbors to queue.
            for neighbor in graph[node]:
                queue.append(neighbor)
                
    return visited_nodes

def dfs(graph, start):
    """
    Traverse the graph using Depth First Search starting from the given node.
    Return the order in which the nodes are visited.
    """
    stack = [start]
    visited_nodes = []
    
    while stack:
        node = stack.pop()
        
        if node not in visited_nodes:
            # Append node to visited nodes
            visited_nodes.append(node)
            
            # Add neighbors to stack.
            # Reversed to maintain order.
            for neighbor in reversed(graph[node]):
                stack.append(neighbor)
                
    return visited_nodes
    
def dijkstra(graph, start):
    """
    Compute the shortest path from the start node to all other nodes in the graph using Dijkstra's algorithm.
    Return a list of minimum distances from the start node to every other node.
    """
    n = len(graph)
    
    dist = [float("inf")] * n
    dist[start] = 0
    
    unvisited = set(range(n))
    while unvisited:
        current = min(unvisited, key = lambda x: dist[x])
        unvisited.remove(current)
        
        for neighbor, weight in enumerate(graph[current]):
            if weight != 0 and neighbor in unvisited:
                new_dist = dist[current] + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
    
    return dist
        
    