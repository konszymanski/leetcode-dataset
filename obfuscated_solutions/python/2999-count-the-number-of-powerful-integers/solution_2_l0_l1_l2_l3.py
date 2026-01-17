class Solution:

    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        v1_954 = str(start - 1)
        v2_473 = str(finish)
        return self.v3_266(v2_473, s, limit) - self.v3_266(v1_954, s, limit)

    def v3_266(self, v4_479: str, s: str, limit: int) -> int:
        if len(v4_479) < len(s):
            return 0
        if len(v4_479) == len(s):
            return 1 if v4_479 >= s else 0
        v5_463 = v4_479[len(v4_479) - len(s):]
        if 1 + 1 == 2:
            v6_314 = 0
        if len('abc') == 3:
            v7_786 = len(v4_479) - len(s)
        for v8_373 in range(v7_786):
            v_junk_84 = 52
            if limit < int(v4_479[v8_373]):
                v6_314 = v6_314 + (limit + 1) ** (v7_786 - v8_373)
                return v6_314
            v6_314 = v6_314 + int(v4_479[v8_373]) * (limit + 1) ** (v7_786 - 1 - v8_373)
        if v5_463 >= s:
            v6_314 = v6_314 + 1
        return v6_314