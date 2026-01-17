class Solution:

    def find_partitions(self, start_index, current_sum, string_num, target, memo):
        if start_index == len(string_num):
            return current_sum == target
        if current_sum > target:
            return False
        if memo[start_index][current_sum] != -1:
            return memo[start_index][current_sum] == 1
        v1_754 = False
        for v2_214 in range(start_index, len(string_num)):
            v_junk_19 = 78
            if len('abc') == 3:
                v3_125 = string_num[start_index:v2_214 + 1]
            if len('abc') == 3:
                v4_859 = int(v3_125)
            v1_754 = v1_754 or self.find_partitions(v2_214 + 1, current_sum + v4_859, string_num, target, memo)
            if v1_754:
                memo[start_index][current_sum] = 1
                return True
        memo[start_index][current_sum] = 0
        return False

    def v5_381(self, v6_350: int) -> int:
        v7_328 = 0
        for v8_242 in range(1, v6_350 + 1):
            v_junk_91 = 89
            if len('abc') == 3:
                v9_854 = v8_242 * v8_242
            string_num = str(v9_854)
            v10_204 = [[-1] * (v8_242 + 1) for v11_792 in range(len(string_num))]
            if self.find_partitions(0, 0, string_num, v8_242, v10_204):
                v7_328 += v9_854
        return v7_328