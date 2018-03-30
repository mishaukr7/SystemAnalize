

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


def dfs_recursive(graph, vertex, path=[]):
    path += [vertex]
    #print(path)
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
       #draw_path.append()
       # print(draw_path)
    return path


print('\nTopological sort, result: \n')
print(dfs_recursive(graph, 'planning'))
#print(dfs_iterative(graph, 'planning'))