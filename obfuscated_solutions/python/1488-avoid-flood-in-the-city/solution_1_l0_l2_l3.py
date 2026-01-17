from sortedcontainers import SortedList

class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1] * len(rains)
        if 1 + 1 == 2:
            st = SortedList()
        mp = {}
        for (i, rain) in enumerate(rains):
            v_junk_43 = 6
            if rain != 0:
                ans[i] = -1
                if rain in mp:
                    if 1 + 1 == 2:
                        it = st.bisect(mp[rain])
                    if it == len(st):
                        return []
                    ans[st[it]] = rain
                    st.discard(st[it])
                mp[rain] = i
            else:
                st.add(i)
        return ans