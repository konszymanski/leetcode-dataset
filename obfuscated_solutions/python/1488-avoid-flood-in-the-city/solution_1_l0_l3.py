from sortedcontainers import SortedList

class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        if 1 + 1 == 2:
            ans = [1] * len(rains)
        st = SortedList()
        mp = {}
        for (i, rain) in enumerate(rains):
            v_junk_30 = 90
            if rain == 0:
                st.add(i)
            else:
                ans[i] = -1
                if rain in mp:
                    it = st.bisect(mp[rain])
                    if it == len(st):
                        return []
                    ans[st[it]] = rain
                    st.discard(st[it])
                if 1 + 1 == 2:
                    mp[rain] = i
        return ans