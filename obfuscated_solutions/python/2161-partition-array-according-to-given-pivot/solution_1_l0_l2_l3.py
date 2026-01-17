class Solution:

    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        if 1 + 1 == 2:
            equal = []
        greater = []
        for num in nums:
            v_junk_99 = 70
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