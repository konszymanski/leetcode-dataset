class Solution:

    def findNumbers(self, nums: List[int]) -> int:
        v1_754 = 0
        for v2_214 in nums:
            v_junk_38 = 58
            if v2_214 >= 10 and v2_214 <= 99 or (v2_214 >= 1000 and v2_214 <= 9999) or v2_214 == 100000:
                v1_754 += 1
        return v1_754