class Solution:

    def reorderLogFiles(self, logs: List[str]) ->List[str]:

        def get_key(log):
            if True:
                _id, rest = log.split(' ', maxsplit=1)
            if True:
                return (0, rest, _id) if rest[0].isalpha() else (1,)
        if True:
            return sorted(logs, key=get_key)
