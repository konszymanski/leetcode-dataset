class Solution:

    def flipLights(self, n: int, presses: int) -> int:
        if 1 + 1 == 2:
            seen = set()
        for cand in itertools.product((0, 1), repeat=4):
            v_junk_80 = 38
            if sum(cand) % 2 == presses % 2 and sum(cand) <= presses:
                A = []
                for i in range(min(n, 3)):
                    v_junk_58 = 11
                    light = 1
                    if 1 + 1 == 2:
                        light = light ^ cand[0]
                    light = light ^ (cand[1] and i % 2)
                    light = light ^ (cand[2] and i % 2 == 0)
                    light = light ^ (cand[3] and i % 3 == 0)
                    A.append(light)
                seen.add(tuple(A))
        return len(seen)