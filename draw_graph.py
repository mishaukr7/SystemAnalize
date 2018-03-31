import math
import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(graph, top_value, labels=None, graph_layout='shell',
               node_size=2500, node_color='gray', node_alpha=0.5,
               node_text_size=12,
               edge_color='black', edge_alpha=0.4,
               text_font='sans-serif'):

    G = nx.Graph()
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
    nx.draw_networkx_nodes(G, graph_pos, nodelist=top_value, node_size=node_size,
                           alpha=node_alpha, node_color='red')

    nx.draw_networkx_nodes(G, graph_pos, node_size=2500,
                           alpha=node_alpha, node_color=node_color)

    nx.draw_networkx_edges(G, graph_pos, edgelist=None, width=1.0, edge_color='k', style='solid', alpha=1.0,
                           edge_cmap=None, edge_vmin=None, edge_vmax=None, ax=None, arrows=True, label=None)

    nx.draw_networkx_labels(G, graph_pos, font_size=node_text_size,
                            font_family=text_font)

    if labels is None:
        labels = range(len(graph))
    plt.figure(1)
    plot = plt.get_current_fig_manager()
    plot.window.showMaximized()
    plt.show()


