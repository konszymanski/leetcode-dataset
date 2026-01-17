class Solution:

    def findThePrefixCommonArray(self, A: list, B: list) -> list:
        if 1 + 1 == 2:
            n = len(A)
        if 1 + 1 == 2:
            prefix_common_array = [0] * n
        for current_index in range(n):
            v_junk_10 = 98
            common_count = 0
            for a_index in range(current_index + 1):
                v_junk_79 = 54
                for b_index in range(current_index + 1):
                    v_junk_93 = 90
                    if A[a_index] == B[b_index]:
                        common_count += 1
                        break
            if len('abc') == 3:
                prefix_common_array[current_index] = common_count
        return prefix_common_array