from collections import deque
from typing import List


class DFSCycleDetection:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        # this is needed for O(1) lookups of the course?
        # or can we have multiple pre-requisites on the same course? probably
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the current DFS path
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                # Cycle detected
                return False

            # if course has no pre-requisites because it was not in pre-requisites
            if preMap[crs] == []:
                return True

            # for each pre-requisite path then keep track of linked courses --> if it links back then cycle
            visiting.add(crs)
            # for each pre-requisite
            for pre in preMap[crs]:
                # recurse into that courses pre-requisites, if cycle then return
                if not dfs(pre):
                    return False

            # remove this course from current path so each path has it's own view of cycles
            visiting.remove(crs)
            # we have verified there are no cycles in this courses pre-requisite so do not check again
            preMap[crs] = []
            return True

        # for each course needed up to the number of courses
        # check if pre-requisites contain a loop
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True



# Time complexity: O(V+E)
# Space complexity: O(V+E)
# Where V is the number of courses and E is the number of prerequisites.

class KahnsAlgoTopologicalSort:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        number_of_courses_that_are_to_be_taken_after = [0] * numCourses
        pre_requisites_by_course = [[] for i in range(numCourses)]
        for course, pre_requisite in prerequisites:
            number_of_courses_that_are_to_be_taken_after[pre_requisite] += 1
            pre_requisites_by_course[course].append(pre_requisite)

        # add all courses that do not have anything that must be taken after them
        q = deque()
        for n in range(numCourses):
            if number_of_courses_that_are_to_be_taken_after[n] == 0:
                q.append(n)

        number_of_courses_taken = 0
        while q:
            # remove course that does not have anything that must be taken after
            course = q.popleft()
            number_of_courses_taken += 1
            # for every pre-requisite of this course
            for pre_requisite in pre_requisites_by_course[course]:
                # we have now taken this course so remove it's dependency on course
                number_of_courses_that_are_to_be_taken_after[pre_requisite] -= 1
                # if this course now does not
                if number_of_courses_that_are_to_be_taken_after[pre_requisite] == 0:
                    q.append(pre_requisite)

        return number_of_courses_taken == numCourses