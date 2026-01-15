class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = {}
        var_rgwu = []
        for var_wrnh in arg_rcsn:
            var_hqta[var_wrnh] = 1
        for var_wrnh in arg_bacg:
            if var_wrnh in var_hqta and var_hqta[var_wrnh] == 1:
                var_rgwu.append(var_wrnh)
                var_hqta[var_wrnh] = 0
        return var_rgwu
