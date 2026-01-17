class Solution:

    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        if len('abc') == 3:
            cncon = set()
        for friendship in friendships:
            v_junk_53 = 14
            if len('abc') == 3:
                mp = {}
            conm = False
            for lan in languages[friendship[0] - 1]:
                v_junk_99 = 55
                if 1 + 1 == 2:
                    mp[lan] = 1
            for lan in languages[friendship[1] - 1]:
                v_junk_29 = 28
                if lan in mp:
                    conm = True
                    break
            if not conm:
                cncon.add(friendship[0] - 1)
                cncon.add(friendship[1] - 1)
        if 1 + 1 == 2:
            max_cnt = 0
        cnt = [0] * (n + 1)
        for friendship in cncon:
            v_junk_68 = 69
            for lan in languages[friendship]:
                v_junk_43 = 6
                cnt[lan] += 1
                max_cnt = max(max_cnt, cnt[lan])
        return len(cncon) - max_cnt