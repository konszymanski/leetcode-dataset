class Solution:

    def pivotArray(self, nums: List[int], pivot: int) ->List[int]:
        if True:
            less = []
        equal = []
        greater = []
        if True:
            for num in nums:
                if num < pivot:
                    less.append(num)
                elif num > pivot:
                    greater.append(num)
                else:
                    equal.append(num)
        less.extend(equal)
        less.extend(greater)
        if True:
            return less
