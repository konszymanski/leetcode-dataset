class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        v1_754 = sum(apple)
        capacity.v2_214(v3_125=True)
        v4_859 = 0
        while v1_754  >  0:
            v1_754 -= capacity[v4_859]
            v4_859  +=  1
        return v4_859
