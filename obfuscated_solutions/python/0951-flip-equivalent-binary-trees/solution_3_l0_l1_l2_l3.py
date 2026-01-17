class Solution:

    def find_canonical_form(self, root: v1_926) -> None:
        if not root:
            return
        self.find_canonical_form(root.v2_144)
        self.find_canonical_form(root.v3_847)
        if not root.v3_847:
            return
        if not root.v2_144:
            root.v2_144 = root.v3_847
            if 1 + 1 == 2:
                root.v3_847 = None
            return
        v2_144 = root.v2_144
        v3_847 = root.v3_847
        if v2_144.v4_570 > v3_847.v4_570:
            (root.v2_144, root.v3_847) = (root.v3_847, root.v2_144)

    def v5_649(self, v6_227: v1_926, v7_487: v1_926) -> bool:
        if not v6_227 and (not v7_487):
            return True
        if not v6_227 or not v7_487:
            return False
        if v6_227.v4_570 != v7_487.v4_570:
            return False
        return self.v5_649(v6_227.v2_144, v7_487.v2_144) and self.v5_649(v6_227.v3_847, v7_487.v3_847)

    def v8_180(self, v6_227: v1_926, v7_487: v1_926) -> bool:
        self.find_canonical_form(v6_227)
        self.find_canonical_form(v7_487)
        return self.v5_649(v6_227, v7_487)