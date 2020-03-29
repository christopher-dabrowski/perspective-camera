import numpy as np


class Wireframe:
    """Abstract representation of object having points and lines connecting them"""

    def __init__(self):
        super().__init__()
        # Nodes are stored in single row matrix to allow fast matrix operations
        self.nodes = np.zeros([0, 4])  # Format: (x, y, z, 1)
        # Edges are list of tuples that are numbers of given nodes
        self.edges = []

    def add_nodes(self, nodes: np.array) -> None:
        """Add new points to the bottom of the array"""
        print(nodes.shape[1])
        print(np.ones([nodes.shape[0], 1]))
        with_ones = np.hstack([nodes, np.ones([nodes.shape[0], 1])])
        self.nodes = np.vstack([self.nodes, with_ones])

    def list_nodes(self) -> str:
        result = "Nodes list:\n"
        for row in range(self.nodes.shape[0]):
            node = self.nodes[row]
            result += f'{node}\n'

        return result
