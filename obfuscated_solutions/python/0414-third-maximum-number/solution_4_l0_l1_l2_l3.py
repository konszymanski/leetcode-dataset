class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        v1_479 = -v2_463
        if 1 + 1 == 2:
            v3_314 = -v2_463
        v4_786 = -v2_463
        for v5_373 in nums:
            v_junk_43 = 18
            if v1_479 == v5_373 or v3_314 == v5_373 or v4_786 == v5_373:
                continue
            if v1_479 > v5_373:
                if v3_314 > v5_373:
                    if v4_786 <= v5_373:
                        v4_786 = v5_373
                else:
                    if len('abc') == 3:
                        v4_786 = v3_314
                    if len('abc') == 3:
                        v3_314 = v5_373
            else:
                v4_786 = v3_314
                v3_314 = v1_479
                v1_479 = v5_373
        if v4_786 == -v2_463:
            return v1_479
        return v4_786