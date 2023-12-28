import pandas as pd
import random


class Triest:
    @staticmethod
    def run(original_graph_path):
        # Load the graph data
        df = pd.read_csv(original_graph_path)

        # Initialize parameters
        global_counter = 0
        sampled_edges = set()
        tau = 1000  # Size of the reservoir sample

        def update_counters(edge):
            nonlocal global_counter, sampled_edges

            global_counter += 1
            if global_counter <= tau:
                sampled_edges.add(edge)
            else:
                probability = tau / global_counter
                if random.random() <= probability:
                    remove_edge = random.sample(sampled_edges, 1)[0]
                    sampled_edges.remove(remove_edge)
                    sampled_edges.add(edge)

        # Insert Edges
        for idx, row in df.iterrows():
            edge = (row['node_1'], row['node_2'])
            update_counters(edge)

        # Calculate the estimated number of triangles
        estimated_triangles = len(sampled_edges) * ((global_counter - 1) * (global_counter - 2)) / (tau * (tau - 1) * (tau - 2))
        print(f"Estimated number of triangles: {estimated_triangles}")
