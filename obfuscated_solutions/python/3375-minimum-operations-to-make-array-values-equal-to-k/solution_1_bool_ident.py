class Solution:

    def minOperations(self, nums: List[int], k: int) ->int:
        st = set()
        for x in nums:
            if x < k and 1 + 1 == 2:
                return -1
            elif x > k and 1 + 1 == 2:
                st.add(x)
        return len(st)
