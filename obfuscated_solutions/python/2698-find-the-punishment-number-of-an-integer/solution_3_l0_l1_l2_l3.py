class Solution:

    def can_partition(self, num, target):
        if target < 0 or num < target:
            return False
        if num == target:
            return True
        return self.can_partition(num // 10, target - num % 10) or self.can_partition(num // 100, target - num % 100) or self.can_partition(num // 1000, target - num % 1000)

    def v1_370(self, v2_926: int) -> int:
        v3_144 = 0
        for v4_847 in range(1, v2_926 + 1):
            v_junk_36 = 86
            v5_570 = v4_847 * v4_847
            if self.can_partition(v5_570, v4_847):
                v3_144 = v3_144 + v5_570
        return v3_144