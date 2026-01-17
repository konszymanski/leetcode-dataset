class Solution:
    def isSubPath(
        self, head: Optional[v1_754], root: Optional[v2_214]
    )  ->  bool:
        if root is None:
            return False
        return self.v3_125(root, head)
    def v3_125(
        self, v4_859: Optional[v2_214], head: Optional[v1_754]
    )  ->  bool:
        if v4_859 is None:
            return False
        if self.v5_381(v4_859, head):
            return True
        return self.v3_125(v4_859.v6_350, head) or self.v3_125(
            v4_859.v7_328, head
        )
    def v5_381(self, v4_859: Optional[v2_214], head: Optional[v1_754])  ->  bool:
        if head is None:
            return True
        if v4_859 is None:
            return False
        if v4_859.v8_242 != head.v8_242:
            return False
        return self.v5_381(v4_859.v6_350, head.next) or self.v5_381(
            v4_859.v7_328, head.next
        )
