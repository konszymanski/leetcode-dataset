class Solution:

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) ->List[int]:
        n = len(A)
        prefix_common_array = [(0) for _ in range(n)]
        frequency = [(0) for _ in range(n + 1)]
        common_count = 0
        current_index = 0
        while current_index < n:
            frequency[A[current_index]] += 1
            if frequency[A[current_index]] == 2:
                common_count += 1
            frequency[B[current_index]] += 1
            if frequency[B[current_index]] == 2:
                common_count += 1
            prefix_common_array[current_index] = common_count
            current_index += 1
        return prefix_common_array
