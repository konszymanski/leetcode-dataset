class Solution:

    def isSubPath(self, head: Optional[v1_532], root: Optional[v2_132]) -> bool:
        if root is None:
            return False
        return self.v3_130(root, head)

    def v3_130(self, v4_195: Optional[v2_132], head: Optional[v1_532]) -> bool:
        if v4_195 is None:
            return False
        if self.v5_323(v4_195, head):
            return True
        return self.v3_130(v4_195.v6_338, head) or self.v3_130(v4_195.v7_617, head)

    def v5_323(self, v4_195: Optional[v2_132], head: Optional[v1_532]) -> bool:
        if head is None:
            return True
        if v4_195 is None:
            return False
        if v4_195.v8_716 != head.v8_716:
            return False
        return self.v5_323(v4_195.v6_338, head.next) or self.v5_323(v4_195.v7_617, head.next)