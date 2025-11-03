from typing import List


class MyInitialSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyDict = {}
        for number in nums:
            frequencyDict[number] = frequencyDict.get(number, 0) + 1

        frequency_element_tuples = []
        for number in frequencyDict.keys():
            frequency_element_tuples.append((frequencyDict[number], number))

        frequency_element_tuples.sort(key=lambda tuple: tuple[0], reverse=True)

        result = []
        for i in range(k):
            if i > len(frequency_element_tuples) - 1:
                break
            result.append(frequency_element_tuples[i][1])
        return result

class SimplifiedDictionarySorting:
    class Solution:
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            frequencyDict = {}
            for number in nums:
                frequencyDict[number] = frequencyDict.get(number, 0) + 1
            print(frequencyDict)

            sortedKeyNumberValueFrequencyTuples = sorted(frequencyDict.items(), key=lambda item: item[1], reverse=True)
            print(sortedKeyNumberValueFrequencyTuples)

            result = []
            for i in range(k):
                if i > len(sortedKeyNumberValueFrequencyTuples) - 1:
                    break
                result.append(sortedKeyNumberValueFrequencyTuples[i][0])
            return result
    # this method still iterates over each element and requires sorting a dict so is O(n log n) time complexity
    # and O(n) space complexity

class BucketSort:
    class Solution:
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            count = {}
            # create a freq buckets up to len(nums) + 1 frequency in case every element is one number
            # this has to be len(nums) + 1 because we are accessing these via index
            # --> the 0th element will not be used as we do not add not seen elements to the freq count
            freq = [[] for i in range(len(nums) + 1)]

            for num in nums:
                count[num] = 1 + count.get(num, 0)
            # add value to corresponding frequency bucket
            for num, cnt in count.items():
                freq[cnt].append(num)
            print(freq)

            res = []
            # this has to be len(freq) - 1 because we are indexing into freq
            for i in range(len(freq) - 1, 0, -1):
                # this iterating does not occur for the empty frequency values
                for num in freq[i]:
                    res.append(num)
                    if len(res) == k:
                        return res