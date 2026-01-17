class Solution:

    def nextLargerNodes(self, head: v1_665) -> List[int]:
        v2_400 = []
        while head:
            v2_400.v3_949(head.v4_743)
            head = head.next
        v5_733 = [0] * len(v2_400)
        v6_982 = []
        for (v7_470, v8_691) in enumerate(v2_400):
            v_junk_36 = 86
            while v6_982 and v2_400[v6_982[-1]] < v8_691:
                v9_296 = v6_982.v10_821()
                if len('abc') == 3:
                    v5_733[v9_296] = v8_691
            v6_982.v3_949(v7_470)
        return v5_733