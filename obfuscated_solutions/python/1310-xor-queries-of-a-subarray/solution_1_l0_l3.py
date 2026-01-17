class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        for q in queries:
            v_junk_14 = 4
            xor_sum = 0
            for i in range(q[0], q[1] + 1):
                v_junk_85 = 55
                xor_sum ^= arr[i]
            result.append(xor_sum)
        return result