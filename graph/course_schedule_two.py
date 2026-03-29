from collections import defaultdict, deque
from typing import List


class FirstAttempt:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = defaultdict(list)
        for prerequisite_set in prerequisites:
            course = prerequisite_set[0]
            prereq = prerequisite_set[1]
            current_prereqs = pre_map[course]
            current_prereqs.append(prereq)
            pre_map[course] = current_prereqs

        print(pre_map)
        course_order = []

        # need to edit to also pass back the path
        def dfs(course: int, seen_courses: List[int], course_order: List[int]):
            if course in seen_courses:
                return False
            if course in course_order:
                return True
            seen_courses.append(course)
            if course in pre_map:
                for req in pre_map[course]:
                    if req not in course_order:
                        if not dfs(req, seen_courses, course_order):
                            return False
            seen_courses.pop()
            pre_map[course] = []
            if course not in course_order:
                course_order.append(course)
            return True

        course_order = []
        for prerequisite_set in prerequisites:
            print(f"looking at pre_req set: {prerequisite_set}")
            course = prerequisite_set[0]
            if not dfs(course, [], course_order):
                return []
            print(f"course order {course_order}")

        if len(course_order) == numCourses:
            return course_order

        for i in range(numCourses):
            if i not in course_order:
                course_order.append(i)
        return course_order


# 32/34 passing, can't see reason why it is failing as test input is too large

class DFSCycleDetection:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        # same pre map for each course to its list of pre-requisites.
        output = []
        # two sets?
        visit, cycle = set(), set()

        def dfs(crs):

            # if we are within a cycle
            if crs in cycle:
                return False
            # if we have already done this course return out without taking further action
            if crs in visit:
                return True

            # add each course to cycle
            cycle.add(crs)
            for pre in prereq[crs]:
                # for each pre-req do dfs
                if dfs(pre) == False:
                    return False
            # remove course from cycle detection
            cycle.remove(crs)
            # mark as visited
            visit.add(crs)
            # add this course to the output
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output


class TopologicalSort:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # prepopulate each course with 0 in degrees or connected courses
        indegree = [0] * numCourses
        # adjacency list
        adj = [[] for i in range(numCourses)]

        # use each course as index into the two lists
        for src, dst in prerequisites:
            # indegree is how many things rely on the dst node
            # or how many courses must be taken after this one (post-requisites)
            indegree[dst] += 1
            # adjacency records the list of nodes that src points to
            adj[src].append(dst)

        q = deque()
        for n in range(numCourses):
            # start with nodes that nothing points to (courses that are not pre-requisites for anything)
            if indegree[n] == 0:
                q.append(n)

        finish, output = 0, []
        while q:
            node = q.popleft()
            # add a node that has no pre-requisite
            output.append(node)
            # increment number of courses taken
            finish += 1
            # for each pre-requisite of the course
            for nei in adj[node]:
                # remove a dependency, the course is taken so no longer has a blocker to take the pointed at course
                indegree[nei] -= 1
                # if course now is not a pre-requisite for anything add to q
                if indegree[nei] == 0:
                    q.append(nei)

        if finish != numCourses:
            return []
        return output[::-1]

# Time complexity: O(V+E)
# Space complexity: O(V+E)

class TopologicalSortWithDFS:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        # This direction of the relationship makes more sense to me
        for nxt, pre in prerequisites:
            # this one has switched the direction of the relationship
            # in degrees is now how many pre-requisites a course has
            indegree[nxt] += 1
            # each course has an adjacency list of courses that must be taken after it
            adj[pre].append(nxt)

        output = []

        def dfs(node):
            # add the node to courses taken
            output.append(node)
            # reduce the number of pre-requisites to -1
            indegree[node] -= 1
            # for each course taken after it
            for nei in adj[node]:
                # they now have one less untaken pre-requisite
                indegree[nei] -= 1
                # if they have no untaken pre-requisites then dfs into them and take them
                if indegree[nei] == 0:
                    dfs(nei)

        # for each course, if it has 0 pre-requisites, then add to course order and add any courses that had it as a pre-req
        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)

        return output if len(output) == numCourses else []