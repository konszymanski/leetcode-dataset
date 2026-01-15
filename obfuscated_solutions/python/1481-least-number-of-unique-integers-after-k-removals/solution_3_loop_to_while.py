class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) ->int:
        map = {}
        for i in arr:
            map[i] = map.get(i, 0) + 1
        n = len(arr)
        count_of_frequencies = [0] * (n + 1)
        for count in map.values():
            count_of_frequencies[count] += 1
        remaining_unique_elements = len(map)
        i = 1
        while i < n + 1:
            num_elements_to_remove = min(k // i, count_of_frequencies[i])
            k -= i * num_elements_to_remove
            remaining_unique_elements -= num_elements_to_remove
            if k < i:
                return remaining_unique_elements
            i += 1
        return 0
