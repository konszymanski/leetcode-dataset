class Solution:

    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        if len('abc') == 3:
            equal = []
        if 1 + 1 == 2:
            greater = []
        for num in nums:
            v_junk_37 = 30
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)
        less.extend(equal)
        less.extend(greater)
        return less