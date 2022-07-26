class GraphNode:
    def __init__(self,val,neighbors=None) -> None:
        self.val = val
        self.neighbors = neighbors or []

class Graph:
    def __init__(self, nodes=None) -> None:
        self.nodes = nodes or []

    # thanks to @trincot from SO, i now have an elegant and
    # much simpler graph inversion solution
    def invert_graph(self):
        for node in self.nodes:
            # create partition on top of existing neighbors.
            # anything that comes before this partition will
            # eventually be deleted
            node.neighbors.append((None, 0))

        for node in self.nodes:
            for i, (neighbor, weight) in enumerate(node.neighbors):
                # once we reach the partition, we're free to
                # delete the stale/original edges
                if neighbor is None:
                    del node.neighbors[:i + 1]  # Remove original edges
                    break
                neighbor.neighbors.append((node, weight))
    
if __name__ == "__main__":
    zero = GraphNode(0)
    one = GraphNode(1)
    two = GraphNode(2)
    three = GraphNode(3)
    four = GraphNode(4)
    five = GraphNode(5)
    six = GraphNode(6)
    zero.neighbors = [(two, 2), (four, 3)]
    one.neighbors = [(three, 1)]
    two.neighbors = [(six, 6)]
    three.neighbors = [(four, 4)]
    four.neighbors = [(one, 1), (six, 4)]
    six.neighbors = [(five, 2)]
    arr = [zero,one,two,three,four,five,six]
    g = Graph(arr)
    g.invert_graph()
    