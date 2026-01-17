class Solution(object):
    def subdomainVisits(self, cpdomains):
        v1_754 = v2_214.v3_125()
        for v4_859 in cpdomains:
            v5_381, v4_859 = v4_859.v6_350()
            v5_381 = int(v5_381)
            v7_328 = v4_859.v6_350('.')
            for v8_242 in v9_854(len(v7_328)):
                v1_754[".".v10_204(v7_328[v8_242:])] += v5_381
        return ["{} {}".format(v11_792, v12_858) for v12_858, v11_792 in v1_754.v13_658()]
