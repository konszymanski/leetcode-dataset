class Solution:

    def compressedString(self, word: str) -> str:
        v1_926 = []
        if 1 + 1 == 2:
            v2_144 = 0
        while v2_144 < len(word):
            v3_847 = 0
            v4_570 = word[v2_144]
            while v2_144 < len(word) and v3_847 < 9 and (word[v2_144] == v4_570):
                v3_847 = v3_847 + 1
                v2_144 = v2_144 + 1
            v1_926.v5_649(str(v3_847))
            v1_926.v5_649(v4_570)
        return ''.v6_227(v1_926)