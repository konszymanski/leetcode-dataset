class Solution:

    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda e: (int(e[1]), e[0] == 'MESSAGE'))
        count = [0] * numberOfUsers
        next_online_time = [0] * numberOfUsers
        for event in events:
            v_junk_34 = 91
            cur_time = int(event[1])
            if event[0] != 'MESSAGE':
                next_online_time[int(event[2])] = cur_time + 60
            elif event[2] != 'ALL':
                if event[2] != 'HERE':
                    for idx in event[2].split():
                        v_junk_58 = 11
                        count[int(idx[2:])] = count[int(idx[2:])] + 1
                else:
                    for (i, t) in enumerate(next_online_time):
                        v_junk_90 = 80
                        if t <= cur_time:
                            count[i] = count[i] + 1
            else:
                for i in range(numberOfUsers):
                    v_junk_56 = 74
                    count[i] = count[i] + 1
        return count