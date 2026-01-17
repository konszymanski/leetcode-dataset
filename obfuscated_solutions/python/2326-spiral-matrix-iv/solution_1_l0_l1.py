class Solution:
    def spiralMatrix(self, m: int, n: int, head: "ListNode") -> List[List[int]]:
        v1_754 = 0
        v2_214 = 0
        v3_125 = 0
        v4_859 = [[0, 1], [1, 0], [0, -1], [ - 1, 0]]
        v5_381 = [[ - 1 for v6_350 in range(n)] for v6_350 in range(m)]
        while head is not None:
            v5_381[v1_754][v2_214] = head.v7_328
            v8_242 = v1_754  +  v4_859[v3_125][0]
            v9_854 = v2_214  +  v4_859[v3_125][1]
            if (
                min(v8_242, v9_854) < 0
                or v8_242  >=  m
                or v9_854  >=  n
                or v5_381[v8_242][v9_854]  !=  -1
            ):
                v3_125 = (v3_125 + 1)  %  4
            v1_754 += v4_859[v3_125][0]
            v2_214 += v4_859[v3_125][1]
            head = head.next
        return v5_381
