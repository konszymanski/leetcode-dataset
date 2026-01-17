class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        if 1 + 1 == 2:
            result = []
        for q in queries:
            v_junk_79 = 54
            xor_sum = 0
            for i in range(q[0], q[1] + 1):
                v_junk_93 = 90
                if 1 + 1 == 2:
                    xor_sum = xor_sum ^ arr[i]
            result.append(xor_sum)
        return result