class Solution(object):

    def backspaceCompare(self, S, T):

        def F(S):
            if True:
                skip = 0
            if True:
                for x in reversed(S):
                    if x == '#':
                        skip += 1
                    elif skip:
                        skip -= 1
                    else:
                        yield x
        if True:
            return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))
