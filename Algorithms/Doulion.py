import pandas as pd
import networkx as nx
from numpy.random import choice
import os


# This algorithm sparsifies a graph by evaluating each edge based on a given value, P.
# For each edge, we decide whether to keep or skip it.
# The resulting graph is then saved as a new graph.

class Doulion:
    @staticmethod
    def Sparsify(original_graph_path, p):
        # Create new Graph
        G = nx.Graph()

        df = pd.read_csv(original_graph_path)
        G = nx.from_pandas_edgelist(df, 'node_1', 'node_2')

        G_sparcified = nx.Graph()

        # Given a p value, add or skip edge
        for edge in G.edges():
            if choice([True, False], p=[p, 1 - p]):
                # Add the edge to the sparsified graph
                G_sparcified.add_edge(edge[0],  edge[1])

        output_path = 'Graphs/Sparcified_Graph.csv'

        # Save new graph
        nx.write_weighted_edgelist(G_sparcified, output_path, delimiter=',')

        # Now open the file again to write the header at the top

        with open(output_path, 'r+') as f:
            content = f.read()  # Read the contents of the file
            f.seek(0, 0)  # Move the cursor to the top of the file
            f.write('node_1,node_2\n' + content)  # Write the header and then the content
