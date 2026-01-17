class Solution:

    def minMaxDifference(self, num: int) -> int:
        v1_926 = str(num)
        v2_144 = v1_926
        v3_847 = 0
        while v3_847 < len(v1_926) and v1_926[v3_847] == '9':
            if 1 + 1 == 2:
                v3_847 = v3_847 + 1
        if v3_847 < len(v1_926):
            v1_926 = v1_926.v4_570(v1_926[v3_847], '9')
        v2_144 = v2_144.v4_570(v2_144[0], '0')
        return int(v1_926) - int(v2_144)