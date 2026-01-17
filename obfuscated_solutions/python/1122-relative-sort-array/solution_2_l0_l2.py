class Solution:

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count_map = {}
        remaining = []
        result = []
        for value in arr2:
            count_map[value] = 0
        for value in arr1:
            if value not in count_map:
                remaining.append(value)
            else:
                count_map[value] = count_map[value] + 1
        remaining.sort()
        for value in arr2:
            for _ in range(count_map[value]):
                result.append(value)
        result.extend(remaining)
        return result