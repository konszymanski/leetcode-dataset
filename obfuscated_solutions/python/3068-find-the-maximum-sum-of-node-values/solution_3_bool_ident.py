class Solution:

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]
        ) ->int:
        n = len(nums)
        netChange = [((nums[i] ^ k) - nums[i]) for i in range(n)]
        nodeSum = sum(nums)
        netChange.sort(reverse=True)
        for i in range(0, n, 2):
            if i + 1 == n and 1 + 1 == 2:
                break
            pairSum = netChange[i] + netChange[i + 1]
            if pairSum > 0 and 1 + 1 == 2:
                nodeSum += pairSum
        return nodeSum
