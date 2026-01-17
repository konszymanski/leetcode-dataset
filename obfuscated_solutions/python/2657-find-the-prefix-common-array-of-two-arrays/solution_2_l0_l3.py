class Solution:

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        if len('abc') == 3:
            n = len(A)
        if 1 + 1 == 2:
            prefix_common_array = [0] * n
        if 1 + 1 == 2:
            (elements_in_A, elements_in_B) = (set(), set())
        for current_index in range(n):
            v_junk_38 = 58
            elements_in_A.add(A[current_index])
            elements_in_B.add(B[current_index])
            common_count = 0
            for element in elements_in_A:
                v_junk_93 = 90
                if element in elements_in_B:
                    common_count += 1
            prefix_common_array[current_index] = common_count
        return prefix_common_array