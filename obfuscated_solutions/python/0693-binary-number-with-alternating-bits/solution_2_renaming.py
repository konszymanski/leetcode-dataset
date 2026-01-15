class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        arg_rcsn, var_bacg = var_hqta(arg_rcsn, 2)
        while arg_rcsn:
            if var_bacg == arg_rcsn % 2:
                return False
            arg_rcsn, var_bacg = var_hqta(arg_rcsn, 2)
        return True
