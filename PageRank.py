import numpy as np

n = 4
graph = np.zeros((n, n), dtype=np.float32)
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'D'),
         ('D', 'C')]
for e in edges:
    u = ord(e[0]) - ord('A')
    v = ord(e[1]) - ord('A')
    graph[u, v] = 1

graph = graph / graph.sum(-1, keepdims=True)
print(graph)
p = np.asarray([0, 0, 0, 1], dtype=np.float32)

assert p.sum() == 1

print('step 1: {}'.format(p))
for _ in range(100):
    p = np.matmul(p, graph)
    print('step {}: {}'.format(_ + 1, p))
