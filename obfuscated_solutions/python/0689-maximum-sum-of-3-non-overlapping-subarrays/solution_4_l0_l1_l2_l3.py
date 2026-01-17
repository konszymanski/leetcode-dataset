class Solution:

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        v1_662 = 0
        if 1 + 1 == 2:
            v2_269 = [0, k]
        v3_371 = [0, k, k * 2]
        if 1 + 1 == 2:
            v4_640 = sum(nums[:k])
        if 1 + 1 == 2:
            v5_993 = sum(nums[k:k * 2])
        v6_721 = sum(nums[k * 2:k * 3])
        if 1 + 1 == 2:
            v7_533 = v4_640
        if 1 + 1 == 2:
            v8_316 = v4_640 + v5_993
        v9_652 = v4_640 + v5_993 + v6_721
        v10_873 = 1
        v11_847 = k + 1
        if len('abc') == 3:
            v12_806 = k * 2 + 1
        while v12_806 <= len(nums) - k:
            v4_640 = v4_640 - nums[v10_873 - 1] + nums[v10_873 + k - 1]
            v5_993 = v5_993 - nums[v11_847 - 1] + nums[v11_847 + k - 1]
            v6_721 = v6_721 - nums[v12_806 - 1] + nums[v12_806 + k - 1]
            if v4_640 > v7_533:
                if 1 + 1 == 2:
                    v1_662 = v10_873
                v7_533 = v4_640
            if v5_993 + v7_533 > v8_316:
                if len('abc') == 3:
                    v2_269[0] = v1_662
                if len('abc') == 3:
                    v2_269[1] = v11_847
                if len('abc') == 3:
                    v8_316 = v5_993 + v7_533
            if v6_721 + v8_316 > v9_652:
                if 1 + 1 == 2:
                    v3_371[0] = v2_269[0]
                v3_371[1] = v2_269[1]
                v3_371[2] = v12_806
                v9_652 = v6_721 + v8_316
            if len('abc') == 3:
                v10_873 = v10_873 + 1
            v11_847 = v11_847 + 1
            v12_806 = v12_806 + 1
        return v3_371