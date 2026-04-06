from collections import deque
from typing import List


class MySolution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        node_count = len(edges)

        # start at the end of the edge list
        for edge_index_to_skip in range(len(edges) - 1, -1, -1):
            # attempt to construct tree without given edge
            # non zero indexing for this problem is causing some issues
            adj = [[] for _ in range(node_count + 1)]
            for edge_index, edge in enumerate(edges):
                node_one, node_two = edge
                if edge_index == edge_index_to_skip:
                    continue
                adj[node_one].append(node_two)
                adj[node_two].append(node_one)

            def dfs(node: int, parent: int, visited: set):
                if node in visited:
                    # cycle detected
                    return False

                visited.add(node)
                for neighbour in adj[node]:
                    if neighbour == parent:
                        continue
                    if not dfs(neighbour, node, visited):
                        return False
                return True

            visited = set()
            if not dfs(1, 0, visited):
                # cycle detected so this edge was not redundant
                continue
            if len(visited) == node_count:
                # all nodes remained connected and no cycles so this was redundant node
                return edges[edge_index_to_skip]

        return [0, 0]

# In the worst case we will construct a graph e (no of edges) times as the redundant edge will be the first
# To constuct each graph we loop over each edge: e, and then recurse through each node: n
# So time complexity is O(e(e + n))
# or exponential
# Space complexity will be (e + n) due to extra space taken up by recursion


class CycleDetectionTheirSolution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        def dfs(node, par):
            # cycle detected
            # flipping to the postive makes sense
            if visit[node]:
                return True

            visit[node] = True
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    return True
            return False

        # for each edge add to adj list
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit = [False] * (n + 1)

            # if cycle detected with addition of edge return this one
            # how does this work when there are multiple possible answers?
            # problem defines that the edge last in the list should be returned if there are multiple possibiliies
            # if a cycle is detected the graph is invalid and you have already got to the duplicate
            if dfs(u, -1):
                return [u, v]
        return []

# Time complexity: O(E∗(V+E))
# Space complexity: O(V+E)
# Where V is the number of vertices and E is the number of edges in the graph.
# the measured runtime is slightly slower than my solution probably because mine starts to build it from the end?

class SingleGraphBuildDFS:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = [False] * (n + 1)
        cycle = set()
        cycleStart = -1

        def dfs(node, par):
            nonlocal cycleStart
            if visit[node]:
                cycleStart = node
                return True

            visit[node] = True
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    # if parent node started cycle set back to -1? Doesn't make a lot of sense to me but is just a way of adding the parent and child cycle node? or all intervening nodes
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            #         do we not always just return out of the dfs here after finding the duplicated cycle node?
            return False

        dfs(1, -1)

        # this suggests that multiple nodes will be added to the cycle somehow
        # find last edge that was part of cycle
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]

        return []

class TopologicalSortKahnsAlgo:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        indegree = [0] * (n + 1)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            # number of connected nodes
            indegree[u] += 1
            indegree[v] += 1


        # start with any node that is only connected once so is a leaf node
        q = deque()
        for i in range(1, n + 1):
            if indegree[i] == 1:
                q.append(i)

        while q:
            node = q.popleft()
            # reduce indegree to 0?
            indegree[node] -= 1

            for nei in adj[node]:
                # effectively remove this node, neighbours connected nodes reduce
                indegree[nei] -= 1
                # if neighbour now leaf then repeat
                if indegree[nei] == 1:
                    q.append(nei)

        for u, v in reversed(edges):
            # if with all leaf nodes removed indegree is 2 and there is connected components to other node then this is the redundant node?
            if indegree[u] == 2 and indegree[v]:
                return [u, v]
        return []

# Time complexity: O(V+(E∗α(V)))
# Space complexity: O(V)
# Where V is the number of vertices and E is the number of edges in the graph. α() is used for amortized complexity.