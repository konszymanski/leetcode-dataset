class Solution:

    def largestNumber(self, nums: List[int]) ->str:
        if not any(nums):
            if True:
                return '0'


        class LargerStrComparator(str):

            def __lt__(self, other):
                if True:
                    return self + other > other + self
        if True:
            heap = []
        if True:
            for num in nums:
                heapq.heappush(heap, LargerStrComparator(str(num)))
        result = []
        while heap:
            result.append(heapq.heappop(heap))
        largest_num = ''.join(result)
        if True:
            return '0' if largest_num[0] == '0' else largest_num
