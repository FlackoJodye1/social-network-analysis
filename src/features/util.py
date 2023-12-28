import networkx as nx


def calculate_key_figures(G: nx.Graph, display=False):
    """
    Calculate key figures for a network graph and optionally display them.

   :param G: A NetworkX graph object.
   :param display: Boolean flag to indicate whether to print the figures.
   :return: A dictionary of calculated key figures.
   """

    num_nodes = len(G.nodes)
    num_edges = len(G.edges)

    # Calculate the average degree
    average_degree = sum(dict(G.degree()).values()) / num_nodes
    # Calculate the average clustering coefficient
    clustering_coefficient = nx.average_clustering(G)

    # Calculate the degree assortativity coefficient
    degree_assortativity_coefficient = nx.degree_assortativity_coefficient(G)

    # Create a dictionary of the values
    key_figures = {
        'number_of_nodes': num_nodes,
        'number_of_edges': num_edges,
        'average_degree': average_degree,
        'average_clustering_coefficient': clustering_coefficient,
        'degree_assortativity_coefficient': degree_assortativity_coefficient
    }

    # print if flag is set to true
    if display:
        print(f"Number of nodes: {num_nodes}")
        print(f"Number of edges: {num_edges}")
        print(f"Average degree: {average_degree}")
        print(f"Average clustering coefficient: {clustering_coefficient}")
        print(f"Degree assortativity coefficient: {degree_assortativity_coefficient}")

    return key_figures
