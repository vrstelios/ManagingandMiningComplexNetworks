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

        for i in node_List:
            neighbors = list(G.neighbors(i))  # found the neighbors
            # creates pairs of neighbours
            node_pairs = [(neighbor1, neighbor2) for idx, neighbor1 in enumerate(neighbors) for neighbor2 in neighbors[idx + 1:]]
            # checked if these pairs are edges in the pair
            for pair in node_pairs:
                if pair in G.edges():
                    triangle_pair_of_root = list(pair) + [i]
                    triangles.add(tuple(sorted(triangle_pair_of_root)))

        print("Triangles are:", triangles, "For Node iterator")
        print("Number of triangles:", len(triangles), "For Node iterator")

        end_time = time.time()
        print("Execution time:", end_time - start_time)

        # Number of triangles: 87254
        # Execution time: 0.9547388553619385
