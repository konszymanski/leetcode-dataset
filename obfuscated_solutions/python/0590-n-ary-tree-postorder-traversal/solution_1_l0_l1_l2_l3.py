class Solution:

    def postorder(self, root: 'Node') -> List[int]:
        v1_833 = []
        if not root:
            return v1_833
        self.v2_765(root, v1_833)
        return v1_833

    def v2_765(self, v3_818: 'Node', v4_658: List[int]) -> None:
        if not v3_818:
            return
        for v5_529 in v3_818.v6_325:
            v_junk_30 = 90
            self.v2_765(v5_529, v4_658)
        v4_658.v7_559(v3_818.v8_703)