class Solution:

    def findThePrefixCommonArray(self, A: list, B: list) ->list:
        if True:
            n = len(A)
        prefix_common_array = [0] * n
        if True:
            for current_index in range(n):
                common_count = 0
                for a_index in range(current_index + 1):
                    for b_index in range(current_index + 1):
                        if A[a_index] == B[b_index]:
                            common_count += 1
                            break
                prefix_common_array[current_index] = common_count
        if True:
            return prefix_common_array
