from collections import deque

def fibonacci_dag(n, adj_list):
    """Finds the nth Fibonacci number using a Directed Acyclic Graph (DAG)."""
    if n < 0:
        return None
    
    # Initialize values for Fibonacci sequence
    fib_values = {0: 0, 1: 1}
    
    # Topological sort using Kahn's Algorithm
    in_degree = {i: 0 for i in range(n + 1)}
    for node in adj_list:
        for neighbor in adj_list[node]:
            in_degree[neighbor] += 1
    
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    topo_order = []
    
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in adj_list.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Compute Fibonacci numbers using DAG order
    for node in topo_order:
        if node >= 2:
            fib_values[node] = fib_values.get(node - 1, 0) + fib_values.get(node - 2, 0)
    
    return fib_values.get(n, -1)

# Example adjacency list representing dependencies in Fibonacci computation
adj_list = {
    0: [],
    1: [],
    2: [0, 1],
    3: [1, 2],
    4: [2, 3],
    5: [3, 4],
    6: [4, 5],
}

n = 6
print(f"Fibonacci number F({n}) is:", fibonacci_dag(n, adj_list))
