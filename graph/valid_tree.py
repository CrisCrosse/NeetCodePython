from collections import defaultdict, deque
from typing import List


class FirstAttempt:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        node_to_nodes = defaultdict(list)
        distinct_nodes = set()

        # two way linkage is fucking me up
        for edge in edges:
            edge.sort()
            source_node = edge[0]
            target_node = edge[1]
            if source_node not in distinct_nodes:
                distinct_nodes.add(source_node)
            if target_node not in distinct_nodes:
                distinct_nodes.add(target_node)
            targets = node_to_nodes[source_node]
            targets.append(target_node)
            node_to_nodes[source_node] = targets

        print(distinct_nodes)
        if len(distinct_nodes) != n:
            return False

        print(node_to_nodes)

        #  can always start at 0?
        def dfs(node, visited):
            if node in visited:
                return False

            visited.add(node)
            dep_nodes = node_to_nodes[node]
            for dep_node in dep_nodes:
                if not dfs(dep_node, visited):
                    return False

            return True

        visited = set()
        if dfs(0, visited):
            print(f"finished recursion, visited: {visited}")
            if len(visited) != n:
                return False
            return True
        return False


class CycleDetection:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if we have more connections than nodes, and input is guaranteed to not be duplicates so there is a double linkage
        # ie a node can be reached via two different paths
        if len(edges) > (n - 1):
            return False

        # create adjacency list on each nodes index, going both ways
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)


        visit = set()

        def dfs(node, parent):
            # if at an already visited node we have double linked + two paths so not a valid tree
            if node in visit:
                return False


            visit.add(node)
            for nei in adj[node]:
                # the use of par is what prevents going back up the tree in the wrong direction, this is what I
                # wasn't sure about when double linking
                # do not go back up the tree
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        # start dfs with 0 node and a non existent parent node, ensure we visited all nodes otherwise unconnected
        return dfs(0, -1) and len(visit) == n


# Time complexity: O(V+E)
# Space complexity: O(V+E)
# V is the number of vertices and E is the number of edges
# we iterate through all the edges to build the adjacency and then also iterate through all the nodes
# in the worst case time complexity (valid tree)

class BreadthFirstSearch:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        # deque of nodes by tree level
        q = deque([(0, -1)])  # (current node, parent node)
        visit.add(0)

        while q:
            # destructure edge
            node, parent = q.popleft()

            # for each adjacent neighbour
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visit:
                    return False
                # add to next level of BFS
                visit.add(nei)
                q.append((nei, node))

        return len(visit) == n
# this approach feels slightly cleaner
# Time complexity: O(V+E)
# Space complexity: O(V+E)


class DSU:
    def __init__(self, n):
        self.comps = n
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False

        self.comps -= 1
        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        return True

    def components(self):
        return self.comps

class DisjointSetUnion:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False
        return dsu.components() == 1

# Time complexity: O(V+(E∗α(V)))
# Space complexity: O(V)
# a() is amortized complexity?