class Solution:
    def check(self, nums: List[int])  ->  bool:
        v1_754 = len(nums)
        if v1_754 <= 1:
            return True
        v2_214 = 0
        for v3_125 in range(1, v1_754):
            if nums[v3_125]  <  nums[v3_125  -  1]:
                v2_214 += 1
                if v2_214 > 1:
                    return False
        if nums[0] < nums[v1_754 - 1]:
            v2_214 += 1
        return v2_214  <=  1
