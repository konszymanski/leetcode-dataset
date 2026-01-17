class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:
        st = set()
        for x in nums:
            v_junk_14 = 4
            if x >= k:
                if x > k:
                    st.add(x)
            else:
                return -1
        return len(st)