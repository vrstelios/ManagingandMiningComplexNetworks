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
        G = nx.from_pandas_edgelist(df, source='node_1', target='node_2')

        G_sparcified = nx.Graph()

        # Given a p value, add or skip edge
        for edge in list(G.edges()):
            result = ["add", "skip"]
            coin_result = choice(result, p=[p, 1-p])

            if coin_result == "add":
                G_sparcified.add_edge(edge[0], edge[1], weight=1 / p)


        output_path = 'Graphs/Sparcified_Graph.csv'

        # Save new graph
        nx.write_edgelist(G_sparcified, output_path)


