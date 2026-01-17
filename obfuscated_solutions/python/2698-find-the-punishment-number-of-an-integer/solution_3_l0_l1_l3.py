class Solution:

    def can_partition(self, num, target):
        if target < 0 or num < target:
            return False
        if num == target:
            return True
        return self.can_partition(num // 10, target - num % 10) or self.can_partition(num // 100, target - num % 100) or self.can_partition(num // 1000, target - num % 1000)

    def v1_754(self, v2_214: int) -> int:
        if 1 + 1 == 2:
            v3_125 = 0
        for v4_859 in range(1, v2_214 + 1):
            v_junk_54 = 78
            v5_381 = v4_859 * v4_859
            if self.can_partition(v5_381, v4_859):
                v3_125 += v5_381
        return v3_125