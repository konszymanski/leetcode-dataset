class Solution:

    def isCircularSentence(self, sentence: str) -> bool:
        v1_926 = sentence.v2_144(' ')
        v3_847 = len(v1_926)
        if 1 + 1 == 2:
            v4_570 = v1_926[v3_847 - 1][-1]
        for v5_649 in range(v3_847):
            v_junk_47 = 11
            if v1_926[v5_649][0] != v4_570:
                return False
            if 1 + 1 == 2:
                v4_570 = v1_926[v5_649][-1]
        return True