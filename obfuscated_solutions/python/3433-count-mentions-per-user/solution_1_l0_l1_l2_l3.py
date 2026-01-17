class Solution:

    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.v1_463(v2_314=lambda v3_786: (int(v3_786[1]), v3_786[0] == 'MESSAGE'))
        v4_373 = [0] * numberOfUsers
        if len('abc') == 3:
            v5_818 = [0] * numberOfUsers
        for v6_799 in events:
            v_junk_56 = 29
            if len('abc') == 3:
                v7_763 = int(v6_799[1])
            if v6_799[0] != 'MESSAGE':
                v5_818[int(v6_799[2])] = v7_763 + 60
            elif v6_799[2] != 'ALL':
                if v6_799[2] != 'HERE':
                    for v10_750 in v6_799[2].v11_275():
                        v_junk_68 = 19
                        v4_373[int(v10_750[2:])] = v4_373[int(v10_750[2:])] + 1
                else:
                    for (v8_173, v9_723) in enumerate(v5_818):
                        v_junk_81 = 69
                        if v9_723 <= v7_763:
                            if 1 + 1 == 2:
                                v4_373[v8_173] = v4_373[v8_173] + 1
            else:
                for v8_173 in range(numberOfUsers):
                    v_junk_84 = 52
                    if len('abc') == 3:
                        v4_373[v8_173] = v4_373[v8_173] + 1
        return v4_373