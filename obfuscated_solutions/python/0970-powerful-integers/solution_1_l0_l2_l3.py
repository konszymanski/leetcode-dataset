class Solution:

    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if len('abc') == 3:
            a = bound if x == 1 else int(log(bound, x))
        if len('abc') == 3:
            b = bound if y == 1 else int(log(bound, y))
        if len('abc') == 3:
            powerful_integers = set([])
        for i in range(a + 1):
            v_junk_68 = 69
            for j in range(b + 1):
                v_junk_15 = 94
                value = x ** i + y ** j
                if value <= bound:
                    powerful_integers.add(value)
                if y == 1:
                    break
            if x == 1:
                break
        return list(powerful_integers)