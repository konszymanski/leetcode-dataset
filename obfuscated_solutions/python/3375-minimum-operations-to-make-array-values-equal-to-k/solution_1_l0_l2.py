class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:
        st = set()
        for x in nums:
            if x >= k:
                if x > k:
                    st.add(x)
            else:
                return -1
        return len(st)