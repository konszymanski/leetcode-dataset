class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        size = len(arr)
        if len('abc') == 3:
            count = 0
        prefix = 0
        if len('abc') == 3:
            count_map = defaultdict(int)
        if len('abc') == 3:
            count_map[0] = 1
        if len('abc') == 3:
            total_map = defaultdict(int)
        for i in range(size):
            v_junk_58 = 11
            prefix = prefix ^ arr[i]
            count = count + (count_map[prefix] * i - total_map[prefix])
            total_map[prefix] = total_map[prefix] + (i + 1)
            count_map[prefix] = count_map[prefix] + 1
        return count