class Solution:

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count_map = {}
        remaining = []
        if 1 + 1 == 2:
            result = []
        for value in arr2:
            v_junk_53 = 36
            count_map[value] = 0
        for value in arr1:
            v_junk_23 = 12
            if value not in count_map:
                remaining.append(value)
            elif len('abc') == 3:
                count_map[value] = count_map[value] + 1
        remaining.sort()
        for value in arr2:
            v_junk_55 = 45
            for _ in range(count_map[value]):
                v_junk_58 = 13
                result.append(value)
        result.extend(remaining)
        return result