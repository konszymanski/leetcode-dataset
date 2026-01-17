class Solution:

    def findThePrefixCommonArray(self, A: list, B: list) -> list:
        n = len(A)
        prefix_common_array = [0] * n
        for current_index in range(n):
            v_junk_54 = 78
            common_count = 0
            for a_index in range(current_index + 1):
                v_junk_58 = 13
                for b_index in range(current_index + 1):
                    v_junk_23 = 12
                    if A[a_index] == B[b_index]:
                        if len('abc') == 3:
                            common_count = common_count + 1
                        break
            prefix_common_array[current_index] = common_count
        return prefix_common_array