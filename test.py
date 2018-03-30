import math
import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(graph, labels=None, graph_layout='shell',
               node_size=2500, node_color='green', node_alpha=0.5,
               node_text_size=12,
               edge_color='blue', edge_alpha=0.4, edge_tickness=2,
               edge_text_pos=0.3,
               text_font='sans-serif'):

    # create networkx graph
    G = nx.Graph()

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    # these are different layouts for the network you may try
    # shell seems to work best
    if graph_layout == 'spring':
        graph_pos=nx.spring_layout(G)
    elif graph_layout == 'spectral':
        graph_pos=nx.spectral_layout(G)
    elif graph_layout == 'random':
        graph_pos=nx.random_layout(G)
    else:
        graph_pos=nx.shell_layout(G)

    # draw graph
    nx.draw_networkx_nodes(G,graph_pos,node_size=node_size,
                           alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                           alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                            font_family=text_font)

    if labels is None:
        labels = range(len(graph))

    edge_labels = dict(zip(graph, labels))
    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels,
                                 label_pos=edge_text_pos)

    # show graph
    plt.figure(1)
    plot = plt.get_current_fig_manager()
    plot.window.showMaximized()
    plt.show()

def toposort(edge_list):
    # edge_set is consummed, need a copy
    edge_set = set([tuple(i) for i in edge_list])
    # node_list will contain the ordered nodes
    node_list = []
    # source_set is the set of nodes with no incomming edges
    node_from_list, node_to_list = zip(*edge_set)
    source_set = set(node_from_list) - set(node_to_list)

    draw_value_list = []
    while len(source_set) != 0:
        # pop node_from off source_set and insert it in node_list
        node_from = source_set.pop()
        node_list.append(node_from)
        # find nodes which have a common edge with node_from
        from_selection = [e for e in edge_set if e[0] == node_from]
        for edge in from_selection:
            # remove the edge from the graph
            node_to = edge[1]
            edge_set.discard(edge)
            #list for draw fucntion

            # if node_to don't have any remaining incomming edge :
            to_selection = [e for e in edge_set if e[1] == node_to]
            if len(to_selection) == 0:
                # add node_to to source_set
                source_set.add(node_to)
            #draw_value_list.append(edge)
            #draw_graph(draw_value_list)
            #print(source_set)

    if len(edge_set) != 0:
        raise IndexError  # not a direct acyclic graph
    else:
        return node_list, draw_value_list


graph_set = [
    ['planning', 'foundation'],
    ['foundation', 'walls'],
    ['walls', 'plumbing'],
    ['walls', 'roof'],
    ['walls', 'electrical wiring'],
    ['plumbing', 'internal decoration'],
    ['plumbing', 'external decoration'],
    ['roof', 'internal decoration'],
    ['roof', 'external decoration'],
    ['electrical wiring', 'internal decoration'],
    ['electrical wiring', 'external decoration'],
    ['internal decoration', 'interior'],
    ['external decoration', 'interior'],
    ['interior', 'settling']
]

print(toposort(graph_set)[0])

#labels = map(chr, range(100, 100 + len(toposort(graph_set)[1])))
#draw_graph(toposort(graph_set)[1])