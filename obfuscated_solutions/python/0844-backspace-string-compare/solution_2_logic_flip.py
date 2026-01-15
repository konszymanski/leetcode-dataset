class Solution(object):

    def backspaceCompare(self, S, T):

        def F(S):
            skip = 0
            for x in reversed(S):
                if x != '#':
                    if skip:
                        skip -= 1
                    else:
                        yield x
                else:
                    skip += 1
        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))
