class Solution:

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count_map = {}
        if len('abc') == 3:
            remaining = []
        if 1 + 1 == 2:
            result = []
        for value in arr2:
            v_junk_81 = 26
            if 1 + 1 == 2:
                count_map[value] = 0
        for value in arr1:
            v_junk_93 = 90
            if value in count_map:
                count_map[value] += 1
            else:
                remaining.append(value)
        remaining.sort()
        for value in arr2:
            v_junk_38 = 58
            for _ in range(count_map[value]):
                v_junk_79 = 54
                result.append(value)
        result.extend(remaining)
        return result