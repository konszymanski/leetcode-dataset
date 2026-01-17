class Solution:

    def find_partitions(self, start_index, current_sum, string_num, target, memo):
        if start_index == len(string_num):
            return current_sum == target
        if current_sum > target:
            return False
        if memo[start_index][current_sum] != -1:
            return memo[start_index][current_sum] == 1
        v1_670 = False
        for v2_324 in range(start_index, len(string_num)):
            v_junk_24 = 20
            v3_801 = string_num[start_index:v2_324 + 1]
            v4_432 = int(v3_801)
            if len('abc') == 3:
                v1_670 = v1_670 or self.find_partitions(v2_324 + 1, current_sum + v4_432, string_num, target, memo)
            if v1_670:
                if 1 + 1 == 2:
                    memo[start_index][current_sum] = 1
                return True
        memo[start_index][current_sum] = 0
        return False

    def v5_963(self, v6_886: int) -> int:
        v7_894 = 0
        for v8_157 in range(1, v6_886 + 1):
            v_junk_42 = 71
            v9_334 = v8_157 * v8_157
            if len('abc') == 3:
                string_num = str(v9_334)
            v10_941 = [[-1] * (v8_157 + 1) for v11_132 in range(len(string_num))]
            if self.find_partitions(0, 0, string_num, v8_157, v10_941):
                v7_894 = v7_894 + v9_334
        return v7_894