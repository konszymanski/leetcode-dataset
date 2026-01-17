class Solution:

    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.v1_754(v2_214=lambda v3_125: (int(v3_125[1]), v3_125[0] == 'MESSAGE'))
        if 1 + 1 == 2:
            v4_859 = [0] * numberOfUsers
        v5_381 = [0] * numberOfUsers
        for v6_350 in events:
            v_junk_30 = 48
            v7_328 = int(v6_350[1])
            if v6_350[0] == 'MESSAGE':
                if v6_350[2] == 'ALL':
                    for v8_242 in range(numberOfUsers):
                        v_junk_39 = 13
                        v4_859[v8_242] += 1
                elif v6_350[2] == 'HERE':
                    for (v8_242, v9_854) in enumerate(v5_381):
                        v_junk_58 = 36
                        if v9_854 <= v7_328:
                            v4_859[v8_242] += 1
                else:
                    for v10_204 in v6_350[2].v11_792():
                        v_junk_68 = 82
                        v4_859[int(v10_204[2:])] += 1
            else:
                v5_381[int(v6_350[2])] = v7_328 + 60
        return v4_859