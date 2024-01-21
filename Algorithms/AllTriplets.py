import time
import pandas as pd
import networkx as nx
import itertools


class FoundAllTriplets:

    @staticmethod
    def found_all_triplets():
        start_time = time.time()

        #df = pd.read_csv('Graphs/tvshow_edges.csv', delimiter=',')
        #df = pd.read_csv('Graphs/ca-GrQc.csv', delimiter=',')
        #df = pd.read_csv('Graphs/new_sites_edges.csv', delimiter=',')
        df = pd.read_csv('Graphs/artist_edges.csv', delimiter=',')
        G = nx.from_pandas_edgelist(df, 'node_1', 'node_2')

        triangles = set()

        for node1 in G:
            for node2 in G[node1]:
                for node3 in G[node2]:
                    # Check if all nodes belong to each other
                    if node1 != node2 and node1 != node3 and node2 != node3:
                        if node1 in G[node2] and node1 in G[node3] and node2 in G[node3]:
                            # Check if the triangle has already been detected
                            triangles.add(tuple(sorted([node1, node2, node3])))

#        for i in range(0, len(edges_list)):
#            for j in range(0, len(edges_list)):
#                # check that have same root
#                if edges_list[i][0] == edges_list[j][0]:
#                    # check there are the graph the two edges
#                    if (edges_list[i][1], edges_list[j][1]) in edges_list:
#                        common_node = edges_list[i][0]
#                        node_i = edges_list[i][1]
#                        node_j = edges_list[j][1]
#                        triangles.add(tuple(sorted([common_node, node_i, node_j])))

        print("Triangles are:", triangles, "For AllTriplets")
        print("Number of triangles:", len(triangles), "For AllTriplets")

        end_time = time.time()
        print("Execution time:", end_time - start_time)

        # ca-GrQc.csv
        # Number of triangles: 48260
        # Execution time: 2.0590288639068604

        # new_sites_edges.csv
        # Number of triangles: 387444
        # Execution time: 68.65653371810913

        # artist_edges.csv
        # Number of triangles: 2273700
        # Execution time: 846.8235864639282

