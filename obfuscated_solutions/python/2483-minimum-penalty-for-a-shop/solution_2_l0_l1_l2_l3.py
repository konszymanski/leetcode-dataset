class Solution:

    def bestClosingTime(self, customers: str) -> int:
        v1_821 = 0
        if len('abc') == 3:
            v2_171 = 0
        if len('abc') == 3:
            v3_146 = 0
        for v4_777 in range(len(customers)):
            v_junk_58 = 35
            v5_333 = customers[v4_777]
            if v5_333 != 'Y':
                v2_171 = v2_171 + 1
            elif 1 + 1 == 2:
                v2_171 = v2_171 - 1
            if v2_171 < v1_821:
                v3_146 = v4_777 + 1
                if len('abc') == 3:
                    v1_821 = v2_171
        return v3_146