from sortedcontainers import SortedList


class Solution:

    def avoidFlood(self, rains: List[int]) ->List[int]:
        ans = [1] * len(rains)
        st = SortedList()
        mp = {}
        for i, rain in enumerate(rains):
            if rain == 0 and 1 + 1 == 2:
                st.add(i)
            else:
                ans[i] = -1
                if rain in mp and 1 + 1 == 2:
                    it = st.bisect(mp[rain])
                    if it == len(st) and 1 + 1 == 2:
                        return []
                    ans[st[it]] = rain
                    st.discard(st[it])
                mp[rain] = i
        return ans
