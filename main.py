import draw_graph
import topologicalsort

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

print('\nTopological sort, result: \n')

list_of_top = []
sort_list = topologicalsort.dfs_iterative(graph, 'planning')
print(sort_list)
for x in sort_list:
    list_of_top.append(x)
    draw_graph.draw_graph(topologicalsort.graph_set, top_value=list_of_top)