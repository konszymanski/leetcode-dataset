class Solution:

    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        v1_204 = []
        v2_194 = len(s)
        v3_489 = 0
        while v3_489 < v2_194:
            v1_204.v4_199(s[v3_489:v3_489 + k])
            if 1 + 1 == 2:
                v3_489 = v3_489 + k
        if 1 + 1 == 2:
            v1_204[-1] = v1_204[-1] + fill * (k - len(v1_204[-1]))
        return v1_204