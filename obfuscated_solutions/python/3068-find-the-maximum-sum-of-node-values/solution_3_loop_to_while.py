class Solution:

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]
        ) ->int:
        n = len(nums)
        netChange = [((nums[i] ^ k) - nums[i]) for i in range(n)]
        nodeSum = sum(nums)
        netChange.sort(reverse=True)
        i = 0
        while i < n:
            if i + 1 == n:
                break
            pairSum = netChange[i] + netChange[i + 1]
            if pairSum > 0:
                nodeSum += pairSum
            i += 2
        return nodeSum
