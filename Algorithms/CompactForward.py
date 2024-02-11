import time
import pandas as pd
import networkx as nx


class CompactForward:

    @staticmethod
    def compact_forward():
        start_time = time.time()

        # df = pd.read_csv('Graphs/tvshow_edges.csv', delimiter=',')
        df = pd.read_csv('Graphs/ca-GrQc.csv', delimiter=',')
        # df = pd.read_csv('Graphs/new_sites_edges.csv', delimiter=',')
        # df = pd.read_csv('Graphs/artist_edges.csv', delimiter=',')
        G = nx.from_pandas_edgelist(df, 'node_1', 'node_2')

        triangles = set()

        for edge in G.edges():
            u, v = edge
            # returns an iterative object providing the common neighbours of nodes u and v
            common_neighbors = nx.common_neighbors(G, u, v)

            for w in common_neighbors:
                # Check if the triangle has already been identified and check accordingly to avoid duplicates
                if u != w and v != w and u != v and w in G[u] and w in G[v] and u in G[v]:
                    triangles.add(tuple(sorted([u, v, w])))


        print("Number of triangles:", len(triangles), "For Compact Forward")

        end_time = time.time()
        print("Execution time:", end_time - start_time)

        # ca-GrQc.csv
        # Number of triangles: 48260
        # Execution time: 1.2880325317382812

        # new_sites_edges.csv
        # Number of triangles: 387444
        # Execution time: 29.88208794593811

        # artist_edges.csv
        # Number of triangles: 2273700
        # Execution time: 328.7054567337036



