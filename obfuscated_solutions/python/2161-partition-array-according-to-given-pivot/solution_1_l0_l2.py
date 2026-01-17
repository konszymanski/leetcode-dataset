class Solution:

    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        greater = []
        for num in nums:
            if num >= pivot:
                if num <= pivot:
                    equal.append(num)
                else:
                    greater.append(num)
            else:
                less.append(num)
        less.extend(equal)
        less.extend(greater)
        return less