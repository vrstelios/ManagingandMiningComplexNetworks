import time
import pandas as pd
import networkx as nx


class FoundNodeIterator:

    @staticmethod
    def found_node_iterator():
        start_time = time.time()

        df = pd.read_csv('Graphs/tvshow_edges.csv', delimiter=',')
        G = nx.from_pandas_edgelist(df, 'node_1', 'node_2')

        node_List = G.nodes()
        triangles = set()
        node_pairs = []

        for i in node_List:
            neighbors = list(G.neighbors(i))  # found the neighbors
            # creates pairs of neighbours
            #for neighbor1 in neighbors:
            #    for neighbor2 in neighbors:
            #        if neighbor1 != neighbor2:
            #            node_pairs.append((neighbor1, neighbor2))
            node_pairs = [(neighbor1, neighbor2) for idx, neighbor1 in enumerate(neighbors) for neighbor2 in neighbors[idx + 1:]]
            # checked if these pairs are edges in the pair
            for pair in node_pairs:
                if G.has_edge(pair[0], pair[1]):
                    triangle_pair_of_root = list(pair) + [i]
                    sorted_triangle = tuple(sorted(triangle_pair_of_root))
                    if sorted_triangle not in triangles:
                        triangles.add(sorted_triangle)

        print("Triangles are:", triangles, "For Node iterator")
        print("Number of triangles:", len(triangles), "For Node iterator")

        end_time = time.time()
        print("Execution time:", end_time - start_time)

        # Number of triangles: 87254
        # Execution time: 0.5020315647125244
