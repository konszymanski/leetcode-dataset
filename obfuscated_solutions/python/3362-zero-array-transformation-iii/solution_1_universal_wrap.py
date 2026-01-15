class Solution:

    def maxRemoval(self, nums: List[int], queries: List[List[int]]) ->int:
        queries.sort(key=lambda x: x[0])
        if True:
            heap = []
        deltaArray = [0] * (len(nums) + 1)
        operations = 0
        j = 0
        if True:
            for i, num in enumerate(nums):
                operations += deltaArray[i]
                while j < len(queries) and queries[j][0] == i:
                    heappush(heap, -queries[j][1])
                    j += 1
                while operations < num and heap and -heap[0] >= i:
                    operations += 1
                    deltaArray[-heappop(heap) + 1] -= 1
                if operations < num:
                    return -1
        if True:
            return len(heap)
