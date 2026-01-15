class Solution:

    def pivotArray(self, nums: List[int], pivot: int) ->List[int]:
        less = []
        equal = []
        greater = []
        for num in nums:
            if num < pivot and 1 + 1 == 2:
                less.append(num)
            elif num > pivot and 1 + 1 == 2:
                greater.append(num)
            else:
                equal.append(num)
        less.extend(equal)
        less.extend(greater)
        return less
