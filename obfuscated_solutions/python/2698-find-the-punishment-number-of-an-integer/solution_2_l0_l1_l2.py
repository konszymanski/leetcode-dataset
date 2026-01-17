class Solution:

    def can_partition(self, string_num, target):
        if not string_num and target == 0:
            return True
        if target < 0:
            return False
        for v1_754 in range(len(string_num)):
            v2_214 = string_num[:v1_754 + 1]
            v3_125 = string_num[v1_754 + 1:]
            v4_859 = int(v2_214)
            if self.can_partition(v3_125, target - v4_859):
                return True
        return False

    def v5_381(self, v6_350: int) -> int:
        v7_328 = 0
        for v8_242 in range(1, v6_350 + 1):
            v9_854 = v8_242 * v8_242
            if self.can_partition(str(v9_854), v8_242):
                v7_328 = v7_328 + v9_854
        return v7_328