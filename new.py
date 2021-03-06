graph = {'planning': set(['foundation']),
         'foundation': set(['walls']),
         'walls': set(['plumbing', 'roof', 'electrical wiring']),
         'plumbing': set(['external decoration', 'internal decoration']),
         'roof': set(['external decoration', 'internal decoration']),
         'electrical wiring': set(['external decoration', 'internal decoration']),
         'internal decoration': set(['interior']),
         'external decoration': set(['interior']),
         'interior': set(['settling']),
         'settling': set([])
         }


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])


print(dfs(graph, 'planning'))