from collections import deque
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
        if not node:
            return None

        oldToNew = {}
        q = deque()
        q.append(node)

        while q:
            old_node = q.popleft()
            print(f"looking at node: {old_node.val}")
            if old_node not in oldToNew:
                new_node = Node(old_node.val)
                print(f"creating new node {new_node.val}")
                oldToNew[old_node] = new_node
            else:
                new_node = oldToNew[old_node]

            new_neighbors = []

            for neighbor in old_node.neighbors:
                print(f"adding neighbor {neighbor.val} to {new_node.val}")
                if neighbor not in oldToNew:
                    new_neighbor = Node(neighbor.val)
                    oldToNew[neighbor] = new_neighbor
                    q.append(neighbor)
                else:
                    new_neighbor = oldToNew[neighbor]
                new_neighbors.append(new_neighbor)
            new_node.neighbors = new_neighbors

        return oldToNew[node]


# Time complexity: O(V+E)
# Space complexity: O(V). Where V is the number of vertices and E is the number of edges.