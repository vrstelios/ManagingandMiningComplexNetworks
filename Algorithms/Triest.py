import pandas as pd
import random
import networkx as nx
class Triest:
    def __init__(self, M):
        self.M = M  # Size of the reservoir
        self.sampled_edges = set()  # Reservoir of sampled edges
        self.global_triangle_count = 0  # Global count of triangles
        self.t = 0  # Total number of edges processed

    # A biased coin flip used in reservoir sampling
    def _flip_biased_coin(self):
        probability = self.M / (self.t + 1)
        return random.random() < probability

    # Handles the insertion of each edge.
    # It uses reservoir sampling to decide whether to keep the new edge.
    # Updates the triangle count accordingly
    def handle_insertion(self, edge):
        self.t += 1
        if len(self.sampled_edges) < self.M or self._flip_biased_coin():
            if len(self.sampled_edges) == self.M:
                self.sampled_edges.remove(random.choice(tuple(self.sampled_edges)))
            self.sampled_edges.add(edge)
            self.update_triangle_count(edge)

    # Checks if a triangle is formed after a new edge insertion.
    # Finds common neighbors of the two nodes in the new edge.
    def update_triangle_count(self, edge):
        u, v = edge
        neighbors_u = {a for a, b in self.sampled_edges if b == u} | {b for a, b in self.sampled_edges if a == u}
        neighbors_v = {a for a, b in self.sampled_edges if b == v} | {b for a, b in self.sampled_edges if a == v}
        common_neighbors = neighbors_u.intersection(neighbors_v)
        self.global_triangle_count += len(common_neighbors)

    # Reads the graph and processes each edge.
    # Print the estimated number of triangles.
    @classmethod
    def run(cls, filepath, M):
        triest_instance = cls(M)
        df = pd.read_csv(filepath)
        for edge in df.itertuples(index=False):
            triest_instance.handle_insertion((edge.node_1, edge.node_2))

        print(f'Estimated number of triangles in the graph: {triest_instance.global_triangle_count}')



