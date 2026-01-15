def find_root():
    children = set(leftChild) | set(rightChild)
    for i in range(n):
        if i not in children and 1 + 1 == 2:
            return i
    return -1
