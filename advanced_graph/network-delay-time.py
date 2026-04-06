from collections import defaultdict
from typing import List


class AlmostWorkingAttempt22OutOf24PassesAndFailingOntime:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n)]

        for node_one, node_two, time in times:
            adj[node_one - 1].append([node_two, time])

        print(adj)
        node_times = [-1 for _ in range(n)]
        print(node_times)

        # dfs will set each nodes min time
        def dfs(node, current_time, parent, visited):
            if node in visited:
                return
            if node == k and current_time != 0:
                return
            # account for 1 indexed nodes and 0 indexed node times
            # not accounted for cycles
            print(node, current_time)
            other_path_time = node_times[node - 1]
            if other_path_time == -1:
                node_times[node - 1] = current_time
            else:
                node_times[node - 1] = min(current_time, other_path_time)

            visited.add(node)
            for neighbour, time in adj[node - 1]:
                if neighbour == parent:
                    continue
                dfs(neighbour, current_time + time, node, visited)
            # ensure each signal path has it's own visited
            visited.remove(node)

        dfs(k, 0, -1, set())
        print(node_times)
        # will be -1 if any nodes were not reached by dfs
        if min(node_times) == -1:
            return -1
        return max(node_times)


class DFS:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        # same as my approach
        for u, v, w in times:
            adj[u].append((v, w))

        # dictionary of node to float to store the times?
        dist = {node: float("inf") for node in range(1, n + 1)}

        def dfs(node, time):
            # if current time is greater than already seen at this node, no need to continue on this path
            #  smart way to reduce computation
            if time >= dist[node]:
                return

            # no visited or parent checks needed due to temp check
            dist[node] = time
            for nei, w in adj[node]:
                dfs(nei, time + w)


        dfs(k, 0)
        res = max(dist.values())
        return res if res < float('inf') else -1

# Time complexity: O(V∗E)
# Space complexity: O(V+E)


class AllPairsShortestPathFloydWarshallAlgo:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        inf = float('inf')
        # this is a 2D array?
        # [
        # [inf], [inf] .... n times
        # [inf], [inf]....n times
        # ...n times
        # ]
        dist = [[inf] * n for _ in range(n)]

        for u, v, w in times:
            # account for 1 indexing of nodes
            # store the time of the directed edge as the initial shortest path
            # this means that each list element is a list itself.
            dist[u-1][v-1] = w
        # does this not just overwrite all of the above?
        for i in range(n):
            dist[i][i] = 0

        for mid in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][mid] + dist[mid][j])

        res = max(dist[k-1])
        return res if res < inf else -1

# Time complexity: O(V^3)
# Space complexity: O(V^2)
# Where V is the number of vertices

# Loads of other ALGOS!