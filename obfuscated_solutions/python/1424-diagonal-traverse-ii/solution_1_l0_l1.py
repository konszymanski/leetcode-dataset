class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        v1_754 = v2_214(list)
        for v3_125 in range(len(nums)  -  1,  - 1, -1):
            for v4_859 in range(len(nums[v3_125])):
                v5_381 = v3_125 + v4_859
                v1_754[v5_381].v6_350(nums[v3_125][v4_859])
        v7_328 = []
        v8_242 = 0
        while v8_242 in v1_754:
            v7_328.v9_854(v1_754[v8_242])
            v8_242  +=  1
        return v7_328
