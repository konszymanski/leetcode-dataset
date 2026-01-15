class MyCircularDeque:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_ihhe.queue = [0] * arg_xdvx
        arg_ihhe.front = 0
        arg_ihhe.rear = arg_xdvx - 1
        arg_ihhe.size = 0
        arg_ihhe.capacity = arg_xdvx

    def func_rcsn(arg_ihhe, arg_bacg):
        if arg_ihhe.isFull():
            return False
        arg_ihhe.front = (arg_ihhe.front - 1 + arg_ihhe.capacity
            ) % arg_ihhe.capacity
        arg_ihhe.queue[arg_ihhe.front] = arg_bacg
        arg_ihhe.size += 1
        return True

    def func_hqta(arg_ihhe, arg_bacg):
        if arg_ihhe.isFull():
            return False
        arg_ihhe.rear = (arg_ihhe.rear + 1) % arg_ihhe.capacity
        arg_ihhe.queue[arg_ihhe.rear] = arg_bacg
        arg_ihhe.size += 1
        return True

    def func_rgwu(arg_ihhe):
        if arg_ihhe.isEmpty():
            return False
        arg_ihhe.front = (arg_ihhe.front + 1) % arg_ihhe.capacity
        arg_ihhe.size -= 1
        return True

    def func_wrnh(arg_ihhe):
        if arg_ihhe.isEmpty():
            return False
        arg_ihhe.rear = (arg_ihhe.rear - 1 + arg_ihhe.capacity
            ) % arg_ihhe.capacity
        arg_ihhe.size -= 1
        return True

    def func_osiz(arg_ihhe):
        if arg_ihhe.isEmpty():
            return -1
        return arg_ihhe.queue[arg_ihhe.front]

    def func_ayzf(arg_ihhe):
        if arg_ihhe.isEmpty():
            return -1
        return arg_ihhe.queue[arg_ihhe.rear]

    def func_wnki(arg_ihhe):
        return arg_ihhe.size == 0

    def func_egyk(arg_ihhe):
        return arg_ihhe.size == arg_ihhe.capacity
