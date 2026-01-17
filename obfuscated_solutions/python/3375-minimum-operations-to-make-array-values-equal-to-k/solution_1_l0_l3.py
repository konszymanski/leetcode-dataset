class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:
        st = set()
        for x in nums:
            v_junk_79 = 12
            if x < k:
                return -1
            elif x > k:
                st.add(x)
        return len(st)