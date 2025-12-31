import heapq
import math
from collections import defaultdict
from typing import List


class BruteForce:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # there is probably a more elegant way to do this sorting --> heap
        distance_to_points = defaultdict(list)
        distances = []

        for point in points:
            x, y = point[0], point[1]
            # x2, y2 is 0 so do not need to subtract
            distance = math.sqrt(pow(x, 2) + pow(y, 2))
            points_with_same_distance = distance_to_points[distance]
            points_with_same_distance.append(point)

            distance_to_points[distance] = points_with_same_distance
            distances.append(distance)

        print(distances, distance_to_points)
        output = []
        distances.sort()
        while k:
            closest_distance = distances[0]
            distances.remove(closest_distance)
            points = distance_to_points[closest_distance]
            while points and k:
                output.append(points.pop())
                k -= 1

        return output

# This solution is worst case O(n log n) time complexity because we sort the list of distances which will use the tim sort algorithm
# using .remove is O(n) time complexity
# This solution is O(3n) space complexity because we create a distances array, a hash map and a output array of size n

class SimplifiedBruteForce:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: math.sqrt(p[0] ** 2 + p[1] ** 2))
        return points[:k]

class UseHeapForDistanceSorting:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # there is probably a more elegant way to do this sorting --> heap
        distance_to_points = defaultdict(list)
        distances = []
        heapq.heapify(distances)

        for point in points:
            x, y = point[0], point[1]
            # x2, y2 is 0 so do not need to subtract
            distance = math.sqrt(pow(x, 2) + pow(y, 2))
            points_with_same_distance = distance_to_points[distance]
            points_with_same_distance.append(point)

            distance_to_points[distance] = points_with_same_distance
            heapq.heappush(distances, distance)

        print(distances, distance_to_points)
        output = []
        while k:
            closest_distance = heapq.heappop(distances)
            points = distance_to_points[closest_distance]
            while points and k:
                output.append(points.pop())
                k -= 1

        return output
# This solution is O(n) time complexity because the heap push and pop is O(log n) time complexity

class MinHeapSimplified:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            # misses out the sqrt
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        # linear time heapify operation
        heapq.heapify(minHeap)
        res = []

        while k > 0:
            # heapq must use the first list element to sort the heap?
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res

# Time Complexity: O(n + k * log n)
# k * log n due to doing log n heap pop operation k times
# Space Complexity: O(n)

class MaxHeap:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            # make each distance negative to switch implementation to max heap, min element still at heap[0]
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, [dist, x, y])
            if len(maxHeap) > k:
                # remove largest absolute value element; furthest from the origin
                heapq.heappop(maxHeap)

        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        return res

# Time complexity O(n∗logk)
# Space complexity O(k)
# we only ever store k elements in the heap so better space, not sure why time complexity improved

class QuickSelect:
    def kClosest(self, points, k):
        euclidean = lambda x: x[0] ** 2 + x[1] ** 2

        def partition(l, r):
            pivotIdx = r
            pivotDist = euclidean(points[pivotIdx])
            i = l
            for j in range(l, r):
                if euclidean(points[j]) <= pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[r] = points[r], points[i]
            return i

        L, R = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = partition(L, R)
            if pivot < k:
                L = pivot + 1
            else:
                R = pivot - 1
        return points[:k]

# This is O(n) average time complexity and worst case O(n ^ 2) time complexity
# It is O(1) space complexity