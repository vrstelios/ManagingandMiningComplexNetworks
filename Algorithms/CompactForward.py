import time
import pandas as pd
import networkx as nx


class FoundCompactForward:

    @staticmethod
    def found_compact_forward():
        start_time = time.time()

        df = pd.read_csv('Graphs/tvshow_edges.csv', delimiter=',')
        G = nx.from_pandas_edgelist(df, 'node_1', 'node_2')

        visited_nodes = set()
        triangles = []

        degrees = sorted(G.degree, key=lambda x: x[1], reverse=True)

        sorted_nodes_by_degree = [node for node, degree in degrees]

        h = {node: position for position, node in enumerate(sorted_nodes_by_degree)}

        for node in sorted_nodes_by_degree:
            visited_nodes.add(node)
            neighbors_node = list(G.neighbors(node))

            # For each node that has not been visited in its neighbours
            for k in [n for n in neighbors_node if n not in visited_nodes]:
                neighbors_k = list(G.neighbors(k))

                i = j = 0
                # looking the neighbors
                while i < len(neighbors_k) and j < len(neighbors_node):
                    # It uses the positions of nodes in the sorted list to identify triangles
                    u_ = neighbors_k[i]
                    v_ = neighbors_node[j]

                    if h[u_] < h[v_]:
                        i += 1
                    elif h[u_] > h[v_]:
                        j += 1
                    else:
                        triangles.append(sorted([k, node, u_]))
                        i += 1
                        j += 1

        triangles_set = list(set(map(tuple, triangles)))
        print("Triangles are:", triangles_set, "For Compact Forward")
        print("Number of triangles:", len(triangles_set), "For Compact Forward")

        end_time = time.time()
        print("Execution time:", end_time - start_time)

        # Number of triangles: 36071
        # Execution time: 0.3381192684173584



