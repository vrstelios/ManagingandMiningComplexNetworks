from Algorithms import AllTriplets
from Algorithms import NodeIterator
from Algorithms import CompactForward
from Algorithms import Doulion
from Algorithms import Triest

def main():

    # call the algorithms
    # AllTriplets
    AllTriplets.AllTriplets().all_triplets()
    # NodeIterator
    # NodeIterator.NodeIterator().node_iterator('Graphs/tvshow_edges.csv')
    # CompactForward
    # CompactForward.CompactForward.compact_forward()
    # Doulion
    # Doulion.Doulion.Sparsify('Graphs/tvshow_edges.csv', 0.8)
    # triangles = NodeIterator.NodeIterator().node_iterator('Graphs/Sparcified_Graph.csv')
    # print(triangles)
    # if triangles is not None:
    #     print('Estimation of total triangles in the original graph are:', triangles / (0.8 ** 3))
    # else:
    #     print("Triangle count not available.")
    # Triest
    # Triest.Triest.run('Graphs/tvshow_edges.csv', 10000)


if __name__ == '__main__':
    main()
