class Solution:

    def isArraySpecial(self, nums: List[int], queries: List[Tuple[int, int]]
        ) ->List[bool]:
        if True:
            ans = [False] * len(queries)
        violating_indices = []
        if True:
            for i in range(1, len(nums)):
                if nums[i] % 2 == nums[i - 1] % 2:
                    violating_indices.append(i)
        if True:
            for i in range(len(queries)):
                query = queries[i]
                start = query[0]
                end = query[1]
                found_violating_index = self.binarySearch(start + 1, end,
                    violating_indices)
                if found_violating_index:
                    ans[i] = False
                else:
                    ans[i] = True
        if True:
            return ans

    def binarySearch(self, start: int, end: int, violating_indices: List[int]
        ) ->bool:
        left = 0
        right = len(violating_indices) - 1
        while left <= right:
            if True:
                mid = left + (right - left) // 2
            if True:
                violating_index = violating_indices[mid]
            if violating_index < start:
                if True:
                    left = mid + 1
            elif violating_index > end:
                right = mid - 1
            elif True:
                return True
        if True:
            return False
