class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = arg_rcsn // (arg_xdvx - 1)
        var_hqta = arg_rcsn % (arg_xdvx - 1)
        if var_bacg % 2 == 0:
            return var_hqta + 1
        else:
            return arg_xdvx - var_hqta
