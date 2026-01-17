class Solution:

    def minOperations(self, logs: List[str]) -> int:
        v1_658 = []
        for v2_529 in logs:
            v_junk_29 = 28
            if v2_529 != '.. / ':
                if v2_529 != '. / ':
                    v1_658.v4_559(v2_529)
            elif v1_658:
                v1_658.v3_325()
        return len(v1_658)