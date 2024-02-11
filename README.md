﻿# ManagingandMiningComplexNetworks

# Algorithms

In this project, we aim to implement and evaluate various algorithms for triangle counting within graphs, focusing on both exact and approximate methodologies. Firstly, we will implement three exact algorithms for triangle counting: 

1) **All Triplets Algorithm:** This method involves checking every possible triplet of nodes in the graph to determine if they form a triangle.
2) **Node Iterator Algorithm:** This approach iterates over each node, examining its neighbors to identify triangles involving the node. 
3) **Compact Forward Algorithm:** A more efficient exact method that exploits the ordering of nodes to reduce the number of comparisons necessary to find triangles. 

Additionally, we will explore an approximate triangle counting method: 

**DOULION Algorithm:** This algorithm introduces a graph sparsification step, reducing the graph's size by randomly removing edges. After sparsification, any of the exact counting algorithms can be applied to estimate the number of triangles in the original graph. Lastly, we will implement a streaming algorithm for triangle counting: 
**TRIEST Algorithm** (Edge Insertions Only): This algorithm is designed for dynamic graphs, where edges are added over time. By maintaining a sample of the edges and updating triangle counts with each insertion, it provides an estimate of the total number of triangles. This project aims to compare these algorithms in terms of accuracy, efficiency, and suitability for different graph sizes and densities. Through this comparison, we will gain insights into the trade-offs between exact and approximate methods for triangle counting and the applicability of streaming algorithms to dynamic graph data.

# Code in review
The organization of our codebase can be outlined as follows:

 1) **Main.py:** The main class serves the entry point for the application. It provides a basic structure for calling and executing the different triangle counting algorithms that were implemented on a graph dataset. It presents the results, detailing the count of triangles identified alongside the corresponding execution time

2) **AllTriplets.py:** Implements the All Triplets algorithm, that is a brute-force method employed for counting triangles in graphs. This approach involves iterating through all possible triplets of nodes within a graph to determine if they form a triangle.

- Imports: The code begins by importing necessary Python libraries. 
        -‘time’ is used to measure the execution time of the algorithm
        -‘pandas’ for reading the graph data from a CSV file
        -‘networkx’ for performing operations, and itertools
- FoundAllTriplets: This class contains a single static method, found_all_triplets(), which implements the triangle counting algorithm.It iterates over each node (node1) in the graph. For every pair of connected nodes (node1, node2), it checks if there is a third node (node3) that forms a triangle with node1 and node2. This is determined by checking if node3 is connected to both node1 and node2.
 
3) **CompactForward.py:** Implements the Compact Forward algorithm for counting triangles in a graph. This algorithm is an improvement over brute-force method ‘All Triplets’, by leveraging the concept of common neighbors between pairs of nodes to efficiently identify triangles.

- Imports: The code begins by importing necessary Python libraries. 
          - ‘time’ is used to measure the execution time of the algorithm
          - ‘pandas’ for reading the graph data from a CSV file
          - ‘networkx’ for performing operations, and itertools
- CompactForward: This class is designed to implement the functionality for finding triangles using the Compact Forward algorithm.

It reads a graph from a CSV file specified by ‘graph_path’ into a pandas DataFrame and then converts this DataFrame into a NetworkX graph. This
graph represents nodes connected by edges. The algorithm iterates over each edge in the graph, utilizing NetworkX's ‘common_neighbors’ function to find nodes (u and v) that share a common neighbor (w). This approach efficiently narrows the search for potential triangles to only those nodes directly connected by an edge and sharing a common neighbor, significantly reducing the computational overhead. If a set of three nodes (u, v, w) forms a triangle, they are added to a set named triangles after being sorted. This sorting ensures uniqueness by preventing the same triangle from being counted multiple times due to different node orderings.

4) **NodeIterator.py:** Implements a triangle counting algorithm known as the Node Iterator.. This algorithm is designed to efficiently identify all triangles (sets of three mutually connected nodes) within a graph.

- Imports: The code begins by importing necessary Python libraries. 
        - ‘time’ is used to measure the execution time of the algorithm
        - ‘pandas’ for reading the graph data from a CSV file
        - ‘networkx’ for performing operations, and itertools
- NodeIterator: This class is designed to implement the functionality for finding triangles using the Node iterator algorithm.

The method iterates over each node in the graph. For a given node, it retrieves a set of its neighbors. It then examines each possible pair of these neighbors (u and w). If u and w are directly connected by an edge (forming a triangle with the original node), the method checks for duplicates and ensures that the triangle is unique before adding it to the triangles set. This uniqueness check involves sorting the nodes of the triangle to prevent the same triangle from being counted more than once due to different node ordering. After examining all nodes and their neighbors, the method prints the set of identified triangles, the total count of triangles, and the execution time.



5) **Doulion.py:** Implements the DOULION algorithm, an approximate method for triangle counting in graphs through graph sparsification. This algorithm is particularly useful for large graphs where exact triangle counting would be computationally expensive. 

- Imports: The code begins by importing necessary Python libraries. 
       - ‘time’ is used to measure the execution time of the algorithm
       - ‘pandas’ for reading the graph data from a CSV file
       - ‘networkx’ for performing operations, and itertools
- Doulion: This class is designed to implement the functionality for estimating the number of triangles using the Doulion algorithm.

The method consists of two major steps:
1) Sparsification: Calls the sparsify method to randomly remove edges from the original graph based on the probability p, resulting in a sparsified graph. 
2) Triangle Counting: Utilizes the CompactForward algorithm (presumably implemented in the Algorithms module) on the sparsified graph to count triangles and then estimates the triangle count on the original bigger graph.



**Triest.py:** Implements the TRIEST algorithm, a technique for estimating the number of triangles in a graph using a fixed-size memory (reservoir). Represents a streaming algorithm approach, as the edges are continuously added over time, and it's impractical to store all the edges due to memory constraints. 
- Imports: The code begins by importing necessary Python libraries. 
        - ‘time’ is used to measure the execution time of the algorithm
        - ‘pandas’ for reading the graph data from a CSV file
        - ‘networkx’ for performing operations, and itertools
- Triest: This class is designed to implement the functionality for estimating the number of triangles using the Triest algorithm.
- _flip_biased_coin: Simulates a biased coin flip to decide whether a new edge should be added to the reservoir. The probability of keeping the edge decreases as more edges are processed, ensuring that the reservoir size remains fixed at M. 
- _insertion Method: Manages the insertion of new edges into the graph. It decides whether to add the new edge to the reservoir based on the result of _flip_biased_coin. If the reservoir is full and a new edge is to be added, an existing edge is randomly removed to make space. This method also updates the global triangle count by calling update_triangle_count. 
update_triangle_count: Updates the estimated number of triangles based on the new edge. It finds common neighbors between the two nodes of the edge within the sampled edges, which helps in identifying new triangles formed with the insertion of the edge.

# Graphs
To provide a more comprehensive depiction of our results, we utilized three different graphs: 

1) GR-QC: Representing a small-scale dataset. 
2) New Sites: Reflecting a dataset of medium size. 
30 Artist: Capturing a large-scale dataset.
   
| Name       | Type       | Nodes  | Edges     | Description                                  |
|------------|------------|--------|-----------|----------------------------------------------|
| GR-QC      | Undirected | 5242   | 14,496    |[Collaboration network of Arxiv General Relativity category](https://snap.stanford.edu/data/ca-GrQc.html) |
| New Sites  | Undirected | 27,917 | 206,259   |[Facebook data from February 13 2018](https://snap.stanford.edu/data/gemsec-Facebook.html)  |
| Artist     | Undirected | 50,515 | 819,306   |[Facebook data from February 13 2018](https://snap.stanford.edu/data/gemsec-Facebook.html)  |
