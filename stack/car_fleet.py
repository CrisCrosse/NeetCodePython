from functools import cmp_to_key
from typing import List


class Solution:
    # I used this for some practice with comparison functions, using cmp_to_key
    # python is only supporting this due to compatibility with python 2 though?
    def sortPositionsAndSpeedsByPosition(self, position_and_speed_1, position_and_speed_2):
        if position_and_speed_1[0] > position_and_speed_2[0]:
            return 1
        elif position_and_speed_1[0] == position_and_speed_2[0]:
            return 0
        else:
            return -1

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positions_and_speeds = []
        for i in range(len(position)):
            # could make this into a class but then can't visualise unles implement toString.
            positions_and_speeds.append((position[i], speed[i]))

        positions_and_speeds.sort(key=lambda position_and_speed: position_and_speed[0])
        print(positions_and_speeds)

        car_fleet_counter = 1
        current_fleet_head = positions_and_speeds[-1]
        hours_for_fleet_head_to_reach_target = (target - current_fleet_head[0]) / current_fleet_head[1]

        for i in range(len(position) - 1, -1, -1):
            current_car = positions_and_speeds[i]
            print(i, current_car)
            hours_for_current_car_to_reach_target = (target - current_car[0]) / current_car[1]
            print(hours_for_fleet_head_to_reach_target, hours_for_current_car_to_reach_target)
            will_overlap = hours_for_current_car_to_reach_target <= hours_for_fleet_head_to_reach_target
            if will_overlap:
                continue
            else:
                car_fleet_counter += 1
                # this is never actually used, only the hours one matters as it bakes in the position + speed
                # current_fleet_head = current_car
                hours_for_fleet_head_to_reach_target = hours_for_current_car_to_reach_target

        return car_fleet_counter

# This solution is O(n log n) because we sort the list (timsort used under the hood), other than that we only iterate
# through the list with an O(n) time complexity.
# THis solution is O(n) space because we create a new list of tuples with length n

