import numpy as np
from typing import List, Tuple
from os import listdir, getcwd
from os.path import isfile, join


def load_models_from_folder(foler_name: str) -> List:
    """Load all files from given foler as wireframes"""

    files = [f for f in listdir(foler_name) if isfile(join(foler_name, f))]
    return [Wireframe.load_from_file(f) for f in files]


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

    def add_edges(self, edge_list: List[Tuple[int, int]]) -> None:
        """Add edges from given of node indexes list"""
        self.edges.extend(edge_list)

    def transform(self, transformation_matrix: np.array) -> None:
        """Apply given transformation to all nodes"""
        self.nodes = self.nodes @ transformation_matrix

    @staticmethod
    def point_to_str(point: np.array) -> str:
        data = ', '.join(map(str, point[:3]))
        return f'({data})'

    def list_nodes(self) -> str:
        result = "Nodes list:\n"
        for row in range(self.nodes.shape[0]):
            node = self.nodes[row]
            result += f'{node}\n'

        return result

    def list_edges(self) -> str:
        result = "Edges list:\n"
        for edge in self.edges:
            a = self.nodes[edge[0]]
            b = self.nodes[edge[1]]

            # result += '{' + ', '.join(map(str, a[:3])) + \
            #     ', ' + ', '.join(map(str, b[:3])) + '},\n'
            result += f'Edge from {Wireframe.point_to_str(a)} to {Wireframe.point_to_str(b)}\n'

        return result

    @staticmethod
    def load_from_file(file_name: str):
        i = 0
        loaded_points = dict()
        loaded_edges = []

        with open(file_name, 'r') as file:
            for line in file.readlines():
                points = [float(p) for p in line.split(', ')]
                start = tuple(points[:3])
                end = tuple(points[3:])

                # print(start)
                # print(end)

                for point in (start, end):
                    if not point in loaded_points:
                        # Save point with new index
                        loaded_points[point] = i
                        i += 1

                loaded_edges.append((loaded_points[start], loaded_points[end]))

        sorted_points = sorted(loaded_points.items(), key=lambda x: x[1])
        # print(sorted_points)
        # print(list(zip(*sorted_points)))
        sorted_points = list(zip(*sorted_points))[0]
        # print(sorted_points)

        wireframe = Wireframe()
        wireframe.add_nodes(np.array(sorted_points))
        wireframe.add_edges(loaded_edges)

        return wireframe
