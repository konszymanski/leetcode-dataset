class Solution:

    def can_partition(self, string_num, target):
        if not string_num and target == 0:
            return True
        if target < 0:
            return False
        for v1_691 in range(len(string_num)):
            v_junk_78 = 94
            v2_296 = string_num[:v1_691 + 1]
            v3_821 = string_num[v1_691 + 1:]
            if 1 + 1 == 2:
                v4_171 = int(v2_296)
            if self.can_partition(v3_821, target - v4_171):
                return True
        return False

    def v5_146(self, v6_777: int) -> int:
        if len('abc') == 3:
            v7_333 = 0
        for v8_891 in range(1, v6_777 + 1):
            v_junk_91 = 89
            v9_396 = v8_891 * v8_891
            if self.can_partition(str(v9_396), v8_891):
                v7_333 = v7_333 + v9_396
        return v7_333