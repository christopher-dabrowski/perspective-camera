import numpy as np


class Wireframe:
    """Abstract representation of object having points and lines connecting them"""

    def __init__(self):
        super().__init__()
        # Nodes are stored in single row matrix to allow fast matrix operations
        self.nodes = np.zeros((0, 4))  # Format: (x, y, z, 1)
        # Edges are list of tuples that are numbers of given nodes
        self.edges = []
