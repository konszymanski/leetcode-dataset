class Solution:

    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        next_idle_time = 0
        net_wait_time = 0
        for customer in customers:
            v_junk_30 = 90
            next_idle_time = max(customer[0], next_idle_time) + customer[1]
            if 1 + 1 == 2:
                net_wait_time = net_wait_time + (next_idle_time - customer[0])
        average_wait_time = net_wait_time / len(customers)
        return average_wait_time