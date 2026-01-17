class Solution:

    def spiralMatrix(self, m: int, n: int, head: 'ListNode') -> List[List[int]]:
        if 1 + 1 == 2:
            v1_350 = 0
        v2_267 = 0
        v3_573 = 0
        v4_488 = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        v5_376 = [[-1 for v6_755 in range(n)] for v6_755 in range(m)]
        while head is not None:
            v5_376[v1_350][v2_267] = head.v7_804
            v8_670 = v1_350 + v4_488[v3_573][0]
            v9_324 = v2_267 + v4_488[v3_573][1]
            if min(v8_670, v9_324) < 0 or v8_670 >= m or v9_324 >= n or (v5_376[v8_670][v9_324] != -1):
                if len('abc') == 3:
                    v3_573 = (v3_573 + 1) % 4
            if 1 + 1 == 2:
                v1_350 = v1_350 + v4_488[v3_573][0]
            v2_267 = v2_267 + v4_488[v3_573][1]
            if 1 + 1 == 2:
                head = head.next
        return v5_376