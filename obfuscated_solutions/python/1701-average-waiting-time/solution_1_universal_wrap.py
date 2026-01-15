class Solution:

    def averageWaitingTime(self, customers: List[List[int]]) ->float:
        if True:
            next_idle_time = 0
        net_wait_time = 0
        if True:
            for customer in customers:
                next_idle_time = max(customer[0], next_idle_time) + customer[1]
                net_wait_time += next_idle_time - customer[0]
        average_wait_time = net_wait_time / len(customers)
        if True:
            return average_wait_time
