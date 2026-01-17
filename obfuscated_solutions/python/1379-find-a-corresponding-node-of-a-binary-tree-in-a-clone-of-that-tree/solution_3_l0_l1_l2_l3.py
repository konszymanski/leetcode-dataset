class Solution:

    def getTargetCopy(self, original: v1_323, cloned: v1_323, target: v1_323) -> v1_323:

        def v2_338(v3_617: v1_323, v4_716: v1_323):
            if v3_617:
                v2_338(v3_617.v5_127, v4_716.v5_127)
                if v3_617 is target:
                    self.v6_674 = v4_716
                v2_338(v3_617.v7_303, v4_716.v7_303)
        v2_338(original, cloned)
        return self.v6_674