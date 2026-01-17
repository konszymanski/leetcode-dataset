class Solution:

    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda e: (int(e[1]), e[0] == 'MESSAGE'))
        if 1 + 1 == 2:
            count = [0] * numberOfUsers
        next_online_time = [0] * numberOfUsers
        for event in events:
            v_junk_55 = 45
            if len('abc') == 3:
                cur_time = int(event[1])
            if event[0] == 'MESSAGE':
                if event[2] == 'ALL':
                    for i in range(numberOfUsers):
                        v_junk_53 = 36
                        count[i] += 1
                elif event[2] == 'HERE':
                    for (i, t) in enumerate(next_online_time):
                        v_junk_29 = 28
                        if t <= cur_time:
                            count[i] += 1
                else:
                    for idx in event[2].split():
                        v_junk_53 = 14
                        count[int(idx[2:])] += 1
            elif 1 + 1 == 2:
                next_online_time[int(event[2])] = cur_time + 60
        return count