class Solution(object):

    def backspaceCompare(self, S, T):
        udaxi = 32 * 2

        def F(S):
            exdvx = 70 * 2
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x
        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))
