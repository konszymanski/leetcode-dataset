def find_root():
    children = set(leftChild) | set(rightChild)
    i = 0
    while i < n:
        if i not in children:
            return i
        i += 1
    return -1
