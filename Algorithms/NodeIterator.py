import time
import pandas as pd
import networkx as nx


class FoundNodeIterator:

    @staticmethod
    def found_node_iterator():
        start_time = time.time()

        #df = pd.read_csv('Graphs/tvshow_edges.csv', delimiter=',')
        df = pd.read_csv('Graphs/ca-GrQc.csv', delimiter=',')
        G = nx.from_pandas_edgelist(df, 'node_1', 'node_2')

        triangles = set()

        for node in G:
            neighbors = set(G.neighbors(node)) # find the neighbors of every node
            for u in neighbors:
                for w in neighbors:
                    # Take all possible pairs of nodes u, w and check if they are connected by an edge
                    if u != w and G.has_edge(u, w):
                        # Check if all nodes belong to each other
                        if node != u and node != w and u != w and node in G[u] and node in G[w] and u in G[w]:
                            triangles.add(tuple(sorted([node, u, w])))

        print("Triangles are:", triangles, "For Node iterator")
        print("Number of triangles:", len(triangles), "For Node iterator")

        end_time = time.time()
        print("Execution time:", end_time - start_time)

        # Number of triangles: 48260
        # Execution time: 1.6099989414215088
