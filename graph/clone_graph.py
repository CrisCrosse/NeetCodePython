from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



class DFS:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def copy_each_node_by_dfs(node):
            if not node:
                return None

            if node in oldToNew:
                return oldToNew[node]

            new_node = Node(node.val)
            oldToNew[node] = new_node

            new_neighbors = []
            neighbors = node.neighbors
            for neighbor in neighbors:
                new_neighbors.append(copy_each_node_by_dfs(neighbor))
            new_node.neighbors = new_neighbors
            return new_node

        return copy_each_node_by_dfs(node)

class BreadthFirstSearch:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return None
