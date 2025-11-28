class TimeMap:

    def __init__(self):
        self.map = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        print(f"setting {key} to {value} at {timestamp}")
        current_value = self.map.get(key, [])
        current_value.append((value, timestamp))
        print(current_value)
        self.map[key] = current_value

    def get(self, key: str, timestamp: int) -> str:
        print(f"getting {key} at {timestamp}")
        if key not in self.map:
            return ""

        all_values_and_timestamps = self.map[key]
        print(all_values_and_timestamps)

        left, right = 0, len(all_values_and_timestamps) - 1
        res = ""
        while left <= right:
            print(f"current result {res}")
            # when i get down to two elements I am getting stuck
            print(f"left {all_values_and_timestamps[left]} , right {all_values_and_timestamps[right]}")
            middle = left + (right - left) // 2
            middle_timestamp_and_value = all_values_and_timestamps[middle]
            middle_timestamp = middle_timestamp_and_value[1]
            middle_value = middle_timestamp_and_value[0]
            print(f"middle {all_values_and_timestamps[middle]}")
            print(f"middle timestamp {middle_timestamp}")

            if middle_timestamp <= timestamp:
                res = middle_value
                left = middle + 1
            else:
                right = middle - 1

        return res

