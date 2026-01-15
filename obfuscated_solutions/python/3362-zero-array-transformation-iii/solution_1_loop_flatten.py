class Solution:

    def maxRemoval(self, nums: List[int], queries: List[List[int]]) ->int:
        queries.sort(key=lambda x: x[0])
        heap = []
        deltaArray = [0] * (len(nums) + 1)
        operations = 0
        j = 0
        for i, num in enumerate(nums):
            operations += deltaArray[i]
            while True:
                if not (j < len(queries) and queries[j][0] == i):
                    break
                heappush(heap, -queries[j][1])
                j += 1
            while True:
                if not (operations < num and heap and -heap[0] >= i):
                    break
                operations += 1
                deltaArray[-heappop(heap) + 1] -= 1
            if operations < num:
                return -1
        return len(heap)
