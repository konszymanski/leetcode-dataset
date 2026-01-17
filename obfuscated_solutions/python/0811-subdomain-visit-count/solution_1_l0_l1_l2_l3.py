class Solution(object):

    def subdomainVisits(self, cpdomains):
        v1_180 = v2_665.v3_400()
        for v4_949 in cpdomains:
            v_junk_56 = 21
            (v5_743, v4_949) = v4_949.v6_733()
            v5_743 = int(v5_743)
            v7_982 = v4_949.v6_733('.')
            for v8_470 in v9_691(len(v7_982)):
                v_junk_68 = 82
                v1_180['.'.v10_296(v7_982[v8_470:])] = v1_180['.'.v10_296(v7_982[v8_470:])] + v5_743
        return ['{} {}'.format(v11_821, v12_171) for (v12_171, v11_821) in v1_180.v13_146()]