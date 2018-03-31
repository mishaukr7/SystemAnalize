import math

def dfs_recursive(graph, vertex, path=[]):
    path += [vertex]
    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = dfs_recursive(graph, neighbor, path)
    return path


def dfs_iterative(graph, start):
    stack, path = [start], []
    draw_path = []
    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)
    return path

graph_set = [
    ('planning', 'foundation'),
    ('foundation', 'walls'),
    ('walls', 'plumbing'),
    ('walls', 'roof'),
    ('walls', 'electrical wiring'),
    ('plumbing', 'internal decoration'),
    ('plumbing', 'external decoration'),
    ('roof', 'internal decoration'),
    ('roof', 'external decoration'),
    ('electrical wiring', 'internal decoration'),
    ('electrical wiring', 'external decoration'),
    ('internal decoration', 'interior'),
    ('external decoration', 'interior'),
    ('interior', 'settling')
]