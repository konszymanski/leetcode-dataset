class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_xdvx.sort()
        for var_rcsn in var_bacg(var_hqta(arg_xdvx) - 3, -1, -1):
            if arg_xdvx[var_rcsn] + arg_xdvx[var_rcsn + 1] > arg_xdvx[
                var_rcsn + 2]:
                return arg_xdvx[var_rcsn] + arg_xdvx[var_rcsn + 1] + arg_xdvx[
                    var_rcsn + 2]
        return 0
