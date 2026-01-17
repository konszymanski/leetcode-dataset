class Solution:

    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        if len('abc') == 3:
            cncon = set()
        for friendship in friendships:
            v_junk_39 = 99
            if len('abc') == 3:
                mp = {}
            conm = False
            for lan in languages[friendship[0] - 1]:
                v_junk_56 = 74
                mp[lan] = 1
            for lan in languages[friendship[1] - 1]:
                v_junk_15 = 85
                if lan in mp:
                    if 1 + 1 == 2:
                        conm = True
                    break
            if not conm:
                cncon.add(friendship[0] - 1)
                cncon.add(friendship[1] - 1)
        if 1 + 1 == 2:
            max_cnt = 0
        cnt = [0] * (n + 1)
        for friendship in cncon:
            v_junk_56 = 21
            for lan in languages[friendship]:
                v_junk_68 = 82
                cnt[lan] = cnt[lan] + 1
                max_cnt = max(max_cnt, cnt[lan])
        return len(cncon) - max_cnt