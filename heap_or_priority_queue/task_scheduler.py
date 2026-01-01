import heapq
from collections import Counter, deque
from typing import List


class BruteForce:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count all tasks
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        # get all tasks we need to process and their freq to iterate through
        frequency_and_index = []
        for i in range(26):
            if count[i] > 0:
                frequency_and_index.append([count[i], i])

        time = 0
        processed = []
        while frequency_and_index:
            task_to_process_index = -1

            # for each remaining task
            for i in range(len(frequency_and_index)):
                n_cycles_ago_or_zero = max(0, time - n)
                task = frequency_and_index[i]
                # if task not processed in last n cycles
                if all(processed[j] != task[1] for j in range(n_cycles_ago_or_zero, time)):
                    # if we haven't yet found a task to process, or this task is  more frequent, process this task
                    if task_to_process_index == -1 or frequency_and_index[task_to_process_index][0] < task[0]:
                        task_to_process_index = i

            time += 1
            cur = -1
            # if we found a task to process, add it to processes, decrement or remove tasks remaining
            if task_to_process_index != -1:
                cur = frequency_and_index[task_to_process_index][1]
                frequency_and_index[task_to_process_index][0] -= 1
                if frequency_and_index[task_to_process_index][0] == 0:
                    frequency_and_index.pop(task_to_process_index)
            processed.append(cur)
        return time

# Time complexity is O(t * n) apparently? where t is the time to process given tasks, and n is the cooldown time

class MaxHeap:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        # remove any reference to task names as only their counts matter
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        cooldown_q = deque()  # pairs of [-cnt, idleTime]

        while maxHeap or cooldown_q:
            time += 1

            if not maxHeap:
                # set time to next tasks cool off time
                time = cooldown_q[0][1]
            else:
                # increment negative count towards 0
                cnt = 1 + heapq.heappop(maxHeap)
                # if not yet 0
                if cnt:
                    # set task to cooldown
                    cooldown_q.append([cnt, time + n])

            # if there is a task in cooldown and it is ready for processing, put it onto the task heap
            if cooldown_q and cooldown_q[0][1] == time:
                heapq.heappush(maxHeap, cooldown_q.popleft()[0])
        return time

class Slots:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        count.sort()
        maxf = count[25]
        # number of idle slots between spacings of the most frequent task
        idle = (maxf - 1) * n

        # for other 24 less frequent tasks
        for i in range(24, -1, -1):
            # the number of idle slots that this task uses is it's frequency or the number of slots
            # if you have lots of elements of high frequency, does this not result in loss of additional slots needed
            # any excess elements would go immediately after the last occurrence fo the task without needing idle slots so this workds
            idle -= min(maxf - 1, count[i])
        # idle slots becomes negative where there are enough tasks to fill the idle gaps, resulting in just len(tasks) time
        return max(0, idle) + len(tasks)

# This solution is O(n) time complexity where n is the number of tasks
# This solution is O(1) space complexity because we create an array of at 26 elements

class MathsSlots:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        # we have maxf - 1 gaps
        maxf = max(count)
        maxCount = 0
        # count how many elements would occupy all gaps between tasks and overflow into next cycle
        for i in count:
            maxCount += 1 if i == maxf else 0

        # the amount of time if there are enough slots is number of gaps * size of gaps (gap and element) plus number of elements after gaps
        time = (maxf - 1) * (n + 1) + maxCount

        # if there were not enough idle slots then we will just overflow and have len(tasks) tasks
        return max(len(tasks), time)