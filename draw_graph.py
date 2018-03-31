import math
import networkx as nx
import matplotlib.pyplot as plt
import topologicalsort


def draw_graph(graph, top_value, graph_layout='shell',
               node_size=2500, node_color='gray', node_alpha=0.3,
               node_text_size=12,
               text_font='sans-serif'):

    G = nx.DiGraph()
    for edge in graph:
        G.add_edge(edge[0], edge[1])

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
                           alpha=0.8, node_color='red')

    nx.draw_networkx_nodes(G, graph_pos, node_size=2500,
                           alpha=node_alpha, node_color=node_color)

    nx.draw_networkx_edges(G, graph_pos, width=1.0, edge_color='black',
                           style='solid', alpha=0.3, arrows=True)

    nx.draw_networkx_labels(G, graph_pos, font_size=node_text_size,
                            font_family=text_font)

    plt.figure(1)
    plt.xticks([])
    plt.yticks([])
    plot = plt.get_current_fig_manager()
    plot.window.showMaximized()
    plt.show()


