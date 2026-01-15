class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = []
        for var_bacg in var_hqta(var_rgwu(arg_xdvx)):
            for var_wrnh in var_hqta(var_rgwu(arg_xdvx)):
                if var_bacg == var_wrnh:
                    continue
                if arg_xdvx[var_bacg] in arg_xdvx[var_wrnh]:
                    var_rcsn.append(arg_xdvx[var_bacg])
                    break
        return var_rcsn
