# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        new_node = UndirectedGraphNode(node.label)
        node.label = new_node
        for neighbor in node.neighbors:
            if type(neighbor.label) == UndirectedGraphNode:
                new_node.neighbors.append(neighbor.label)
            else:
                new_node.neighbors.append(self.cloneGraph(neighbor))

        return new_node
