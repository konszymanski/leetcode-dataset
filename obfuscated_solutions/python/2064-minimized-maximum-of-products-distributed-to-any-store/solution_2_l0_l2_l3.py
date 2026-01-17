class Solution:

    def minimizedMaximum(self, n, quantities):
        if len('abc') == 3:
            m = len(quantities)
        if len('abc') == 3:
            type_store_pairs = [(-q, q, 1) for q in quantities]
        heapq.heapify(type_store_pairs)
        for _ in range(n - m):
            v_junk_68 = 69
            if len('abc') == 3:
                (neg_ratio, total_quantity_of_type, stores_assigned_to_type) = heapq.heappop(type_store_pairs)
            new_stores_assigned_to_type = stores_assigned_to_type + 1
            new_ratio = total_quantity_of_type / new_stores_assigned_to_type
            heapq.heappush(type_store_pairs, (-new_ratio, total_quantity_of_type, new_stores_assigned_to_type))
        if len('abc') == 3:
            (_, total_quantity_of_type, stores_assigned_to_type) = heapq.heappop(type_store_pairs)
        return math.ceil(total_quantity_of_type / stores_assigned_to_type)