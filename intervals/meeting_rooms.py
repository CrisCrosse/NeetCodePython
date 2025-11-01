from typing import List
# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end




class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        used_minutes = set()

        for interval in intervals:
            # 1,7 4,5, 6,7 , 8,9, 9,10 has to account for meetings able to start and end on same time, but not able to have a meeting run over the start or end time
            for minute in range(interval.start + 1, interval.end):
                if str(minute) + "middle" in used_minutes:
                    return False
                if str(minute) + "start" in used_minutes:
                    return False
                if str(minute) + "end" in used_minutes:
                    return False
                used_minutes.add(str(minute) + "middle")

            if str(interval.start) + "start" in used_minutes:
                return False
            used_minutes.add(str(interval.start) + "start")
            if str(interval.end) + "end" in used_minutes:
                return False
            used_minutes.add(str(interval.end) + "end")

        return True

#     this is O(n * m) as we iterate over every interval and the range between the meetings




class BruteForceSolution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        for i in range(n):
            A = intervals[i]
            for j in range(i + 1, n):
                B = intervals[j]
                if min(A.end, B.end) > max(A.start, B.start):
                    return False
        return True

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False
        return True


