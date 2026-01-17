class Solution:
    def can_place_balls(self, x, position, m):
        v1_754 = position[0]
        v2_214 = 1
        for v3_125 in range(1, len(position)):
            v4_859 = position[v3_125]
            if v4_859  -  v1_754  >=  x:
                v2_214  +=  1
                v1_754 = v4_859
            if v2_214  ==  m:
                return True
        return False
    def v5_381(self, position: List[int], m: int) -> int:
        v6_350 = 0
        v7_328 = len(position)
        position.v8_242()
        v9_854 = 1
        v10_204 = int(position[ - 1]  /  (m  -  1.0)) + 1
        while v9_854 <= v10_204:
            v11_792 = v9_854 + (v10_204 - v9_854) // 2
            if self.can_place_balls(v11_792, position, m):
                v6_350 = v11_792
                v9_854 = v11_792  +  1
            else:
                v10_204 = v11_792  -  1
        return v6_350
