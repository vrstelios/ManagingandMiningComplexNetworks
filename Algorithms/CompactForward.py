import time
import pandas as pd
import networkx as nx


class FoundCompactForward:

    @staticmethod
    def found_compact_forward():
        start_time = time.time()

        df = pd.read_csv('Graphs/tvshow_edges.csv', delimiter=',')
        G = nx.from_pandas_edgelist(df, 'node_1', 'node_2')

        node_List = G.nodes()



        print("veros")