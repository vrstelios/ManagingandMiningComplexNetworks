import time
import pandas as pd
import networkx as nx


class FoundAllTriplets:

    @staticmethod
    def found_all_triplets():
        start_time = time.time()

        df = pd.read_csv('Graphs/tvshow_edges.csv', delimiter=',')
        G = nx.from_pandas_edgelist(df, 'node_1', 'node_2')

        edges_list = list(G.edges())
        triangles = set()

        for i in range(0, len(edges_list)-1):
            for j in range(0, len(edges_list)-1):
                # check that have same root
                if edges_list[i][0] == edges_list[j][0]:
                    # check there are the graph the two edges
                    if (edges_list[i][1], edges_list[j][1]) in edges_list:
                        common_node = edges_list[i][0]
                        node_i = edges_list[i][1]
                        node_j = edges_list[j][1]
                        triangles.add(tuple(sorted([common_node, node_i, node_j])))

        print("Triangles are:", triangles, "For AllTriplets")
        print("Number of triangles:", len(triangles), "For AllTriplets")

        end_time = time.time()
        print("Execution time:", end_time - start_time)

        # Number of triangles: 87276
        # Execution time: 161.6605236530304
