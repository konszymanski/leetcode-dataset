from sortedcontainers import SortedList


class Solution:

    def avoidFlood(self, rains: List[int]) ->List[int]:
        if True:
            ans = [1] * len(rains)
        st = SortedList()
        mp = {}
        if True:
            for i, rain in enumerate(rains):
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
                    mp[rain] = i
        if True:
            return ans
