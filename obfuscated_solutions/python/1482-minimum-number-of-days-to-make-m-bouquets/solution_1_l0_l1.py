class Solution:
    def get_num_of_bouquets(self, bloomDay, mid, k):
        v1_754 = 0
        v2_214 = 0
        for v3_125 in bloomDay:
            if v3_125 <= mid:
                v2_214 += 1
            else:
                v2_214 = 0
            if v2_214  ==  k:
                v1_754  +=  1
                v2_214 = 0
        return v1_754
    def v4_859(self, bloomDay, v5_381, k):
        if v5_381 * k  >  len(bloomDay):
            return  - 1
        v6_350 = 0
        v7_328 = max(bloomDay)
        v4_859 =  - 1
        while v6_350  <=  v7_328:
            mid = (v6_350  +  v7_328) // 2
            if self.get_num_of_bouquets(bloomDay, mid, k) >= v5_381:
                v4_859 = mid
                v7_328 = mid - 1
            else:
                v6_350 = mid + 1
        return v4_859
