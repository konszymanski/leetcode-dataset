class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = 0
        for var_bacg in var_hqta(var_rgwu(arg_xdvx)):
            if (var_bacg == 0 or arg_xdvx[var_bacg - 1] == ' ') and arg_xdvx[
                var_bacg] != ' ':
                var_rcsn += 1
        return var_rcsn
