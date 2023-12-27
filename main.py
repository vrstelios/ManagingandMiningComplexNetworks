from Algorithms import AllTriplets
from Algorithms import NodeIterator
from Algorithms import CompactForward
from Algorithms import Doulion

def main():
    # call the algorithms
    # AllTriplets
    #AllTriplets.FoundAllTriplets().found_all_triplets()
    # NodeIterator
    #NodeIterator.FoundNodeIterator().found_node_iterator()
    # CompactForward
    #CompactForward.FoundCompactForward.found_compact_forward()
    #Doulion
    result = Doulion.Doulion.Sparcify('Graphs/tvshow_edges.csv', 0.8)
    print(result)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
