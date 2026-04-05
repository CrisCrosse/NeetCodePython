from collections import deque
from typing import List


class MySolution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for edge in edges:
            a, b = edge
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node: int, visited: set):
            visited.add(node)

            for neighbour in adj[node]:
                if neighbour in visited:
                    continue
                dfs(neighbour, visited)

        visited = set()
        component_count = 0
        for edge in edges:
            start_node = edge[0]
            if start_node not in visited:
                component_count += 1
                # dfs will mark all nodes in the component as visited
                dfs(start_node, visited)

        # account for nodes with no edges
        component_count += n - len(visited)
        return component_count

# time complexity is 1 * edge count (adjacency list) +  1 * node count (DFS)

class DFSSolution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        # using a visit flag list instead of a set
        visit = [False] * n
        # destructuring in the for each loop is nice
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            # for all connected nodes
            for nei in adj[node]:
                if not visit[nei]:
                    # if not already visited, mark as visited and continue connected dfs
                    visit[nei] = True
                    dfs(nei)

        res = 0
        # for every node instead for each edge, nice that you do not need to account for the leftover individual ones
        for node in range(n):

            if not visit[node]:
                visit[node] = True
                # call the dfs on every node not yet visited even individual nodes, dfs will do nothing as adj yields no neighbours
                dfs(node)
                res += 1
        return res

# Time complexity: O(V+E)
# Space complexity: O(V+E)
# Where V is the number of vertices and E is the number of edges in the graph.


class BreadthFirstSearchSolution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            # new breadth first search on each start node
            q = deque([node])
            visit[node] = True
            while q:
                cur = q.popleft()
                for nei in adj[cur]:
                    if not visit[nei]:
                        visit[nei] = True
                        q.append(nei)

        res = 0
        for node in range(n):
            if not visit[node]:
                bfs(node)
                res += 1
        return res


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        # find parent node
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            # in the same set already so do nothing
            return False
        # ig parent of v has higher rank than parent u then swap the parents
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        # parent of v is now parent of u
        self.parent[pv] = pu
        # add all the nodes that were in v to u rank
        self.rank[pu] += self.rank[pv]
        return True

class DisjointSetUnion:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create union set of size n
        dsu = DSU(n)
        # at first assume all are individual components
        res = n
        for u, v in edges:
            # if nodes were not in the same set, then reduce connected components because we have now merged them
            if dsu.union(u, v):
                res -= 1
        return res

# Time complexity: O(V+(E∗α(V)))
# Space complexity: O(V)
# Where VV is the number of vertices and EE is the number of edges in the graph. α()α() is used for amortized complexity.