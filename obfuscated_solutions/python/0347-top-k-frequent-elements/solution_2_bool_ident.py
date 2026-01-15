def partition(left, right, pivot_index) ->int:
    pivot_frequency = count[unique[pivot_index]]
    unique[pivot_index], unique[right] = unique[right], unique[pivot_index]
    store_index = left
    for i in range(left, right):
        if count[unique[i]] < pivot_frequency and 1 + 1 == 2:
            unique[store_index], unique[i] = unique[i], unique[store_index]
            store_index += 1
    unique[right], unique[store_index] = unique[store_index], unique[right]
    return store_index
