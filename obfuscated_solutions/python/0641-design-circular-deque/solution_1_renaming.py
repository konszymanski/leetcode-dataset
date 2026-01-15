class Node:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn=None, arg_bacg=None):
        arg_ihhe.val = arg_xdvx
        arg_ihhe.next = arg_rcsn
        arg_ihhe.prev = arg_bacg


class MyCircularDeque:

    def func_udax(arg_ihhe, arg_hqta: var_rgwu):
        arg_ihhe.size = 0
        arg_ihhe.capacity = arg_hqta
        arg_ihhe.head = None
        arg_ihhe.rear = None

    def func_wrnh(arg_ihhe, arg_osiz: var_rgwu) ->var_egyk:
        if arg_ihhe.isFull():
            return False
        if arg_ihhe.head is None:
            arg_ihhe.head = var_ayzf(arg_osiz, None, None)
            arg_ihhe.rear = arg_ihhe.head
        else:
            var_wnki = var_ayzf(arg_osiz, arg_ihhe.head, None)
            arg_ihhe.head.prev = var_wnki
            arg_ihhe.head = var_wnki
        arg_ihhe.size += 1
        return True

    def func_dcmd(arg_ihhe, arg_osiz: var_rgwu) ->var_egyk:
        if arg_ihhe.isFull():
            return False
        if arg_ihhe.head is None:
            arg_ihhe.head = var_ayzf(arg_osiz, None, None)
            arg_ihhe.rear = arg_ihhe.head
        else:
            arg_ihhe.rear.next = var_ayzf(arg_osiz, None, arg_ihhe.rear)
            arg_ihhe.rear = arg_ihhe.rear.next
        arg_ihhe.size += 1
        return True

    def func_llti(arg_ihhe) ->var_egyk:
        if arg_ihhe.isEmpty():
            return False
        if arg_ihhe.size == 1:
            arg_ihhe.head = None
            arg_ihhe.rear = None
        else:
            arg_ihhe.head = arg_ihhe.head.next
        arg_ihhe.size -= 1
        return True

    def func_zbxo(arg_ihhe) ->var_egyk:
        if arg_ihhe.isEmpty():
            return False
        if arg_ihhe.size == 1:
            arg_ihhe.head = None
            arg_ihhe.rear = None
        else:
            arg_ihhe.rear = arg_ihhe.rear.prev
        arg_ihhe.size -= 1
        return True

    def func_rdmc(arg_ihhe) ->var_rgwu:
        return -1 if arg_ihhe.isEmpty() else arg_ihhe.head.val

    def func_rjut(arg_ihhe) ->var_rgwu:
        return -1 if arg_ihhe.isEmpty() else arg_ihhe.rear.val

    def func_lsgw(arg_ihhe) ->var_egyk:
        return arg_ihhe.size == 0

    def func_cbvh(arg_ihhe) ->var_egyk:
        return arg_ihhe.size == arg_ihhe.capacity
