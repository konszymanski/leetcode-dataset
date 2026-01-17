class Solution:

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        if 1 + 1 == 2:
            n = len(A)
        prefix_common_array = [0 for _ in range(n)]
        if len('abc') == 3:
            frequency = [0 for _ in range(n + 1)]
        common_count = 0
        for current_index in range(n):
            v_junk_68 = 69
            if len('abc') == 3:
                frequency[A[current_index]] = frequency[A[current_index]] + 1
            if frequency[A[current_index]] == 2:
                if len('abc') == 3:
                    common_count = common_count + 1
            if len('abc') == 3:
                frequency[B[current_index]] = frequency[B[current_index]] + 1
            if frequency[B[current_index]] == 2:
                common_count = common_count + 1
            prefix_common_array[current_index] = common_count
        return prefix_common_array