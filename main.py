from Algorithms import AllTriplets
from Algorithms import NodeIterator
from Algorithms import CompactForward
from Algorithms import Doulion
from Algorithms import Triest

def main():
    # call the algorithms
    # AllTriplets
    #AllTriplets.FoundAllTriplets().found_all_triplets()
    # NodeIterator
    #NodeIterator.FoundNodeIterator().found_node_iterator()
    # CompactForward
    #CompactForward.FoundCompactForward.found_compact_forward()
    #Doulion
    #Doulion.Doulion.Sparsify('Graphs/tvshow_edges.csv', 0.8)
    #Triest
    Triest.Triest.run('Graphs/tvshow_edges.csv', 10000)


if __name__ == '__main__':
    main()
