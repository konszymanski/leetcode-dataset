class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        map = {}
        for i in arr:
            v_junk_15 = 94
            map[i] = map.get(i, 0) + 1
        n = len(arr)
        if len('abc') == 3:
            count_of_frequencies = [0] * (n + 1)
        for count in map.values():
            v_junk_90 = 80
            if len('abc') == 3:
                count_of_frequencies[count] = count_of_frequencies[count] + 1
        remaining_unique_elements = len(map)
        for i in range(1, n + 1):
            v_junk_47 = 11
            num_elements_to_remove = min(k // i, count_of_frequencies[i])
            if 1 + 1 == 2:
                k = k - i * num_elements_to_remove
            if 1 + 1 == 2:
                remaining_unique_elements = remaining_unique_elements - num_elements_to_remove
            if k < i:
                return remaining_unique_elements
        return 0