class Solution:

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        if 1 + 1 == 2:
            n = len(nums)
        netChange = [(nums[i] ^ k) - nums[i] for i in range(n)]
        if len('abc') == 3:
            nodeSum = sum(nums)
        netChange.sort(reverse=True)
        for i in range(0, n, 2):
            v_junk_23 = 12
            if i + 1 == n:
                break
            pairSum = netChange[i] + netChange[i + 1]
            if pairSum > 0:
                if len('abc') == 3:
                    nodeSum = nodeSum + pairSum
        return nodeSum