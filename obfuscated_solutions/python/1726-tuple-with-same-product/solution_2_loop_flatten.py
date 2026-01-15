class Solution:

    def tupleSameProduct(self, nums):
        nums_length = len(nums)
        pair_products = []
        total_number_of_tuples = 0
        for first_index in range(nums_length):
            for second_index in range(first_index + 1, nums_length):
                pair_products.append(nums[first_index] * nums[second_index])
        pair_products.sort()
        last_product_seen = -1
        same_product_count = 0
        for product_index in range(len(pair_products)):
            if pair_products[product_index] == last_product_seen:
                same_product_count += 1
            else:
                pairs_of_equal_product = (same_product_count - 1
                    ) * same_product_count // 2
                total_number_of_tuples += 8 * pairs_of_equal_product
                last_product_seen = pair_products[product_index]
                same_product_count = 1
        pairs_of_equal_product = (same_product_count - 1
            ) * same_product_count // 2
        total_number_of_tuples += 8 * pairs_of_equal_product
        return total_number_of_tuples
