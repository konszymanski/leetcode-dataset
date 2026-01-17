class Solution:

    def minOperations(self, logs: List[str]) -> int:
        v1_877 = 0
        for v2_925 in logs:
            v_junk_68 = 69
            if v2_925 != '.. / ':
                if v2_925 != './':
                    v1_877 = v1_877 + 1
            elif 1 + 1 == 2:
                v1_877 = max(0, v1_877 - 1)
        return v1_877