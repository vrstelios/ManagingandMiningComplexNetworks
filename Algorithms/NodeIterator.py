import time
import pandas as pd
import networkx as nx


class FoundNodeIterator:

    @staticmethod
    def found_node_iterator():
        start_time = time.time()

        df = pd.read_csv('Graphs/ca-GrQc.csv', delimiter=',')
        G = nx.from_pandas_edgelist(df, 'node_1', 'node_2')

        triangles = []
        visited_nodes = set()

        # Επιλέγουμε τον επόμενο κόμβο (v) για έλεγχο
        for v in G.nodes():
            if v in visited_nodes:
                continue

            visited_nodes.add(v)
            # Παίρνουμε όλα τα ζευγάρια γειτόνων (u, w) του κόμβου v
            neighbors_v = list(G.neighbors(v))
            for i in range(len(neighbors_v)):
                u = neighbors_v[i]
                for j in range(i + 1, len(neighbors_v)):
                    w = neighbors_v[j]

                    # Ελέγχουμε αν υπάρχει ακμή μεταξύ των u και w
                    if G.has_edge(u, w):
                        # Αν υπάρχει ακμή, τότε υπάρχει τρίγωνο
                        triangles.append((v, u, w))
                        # Επιλέξτε ανάλογα με τις απαιτήσεις σας για εκτύπωση ή αποθήκευση

        print("Triangles are:", triangles, "For Node iterator")
        print("Number of triangles:", len(triangles), "For Node iterator")

        end_time = time.time()
        print("Execution time:", end_time - start_time)

        # Number of triangles: 87254
        # Execution time: 0.9547388553619385
