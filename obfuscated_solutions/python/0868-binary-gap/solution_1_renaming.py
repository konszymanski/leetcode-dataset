class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = [var_hqta for var_hqta in var_rgwu(32) if arg_rcsn >>
            var_hqta & 1]
        if var_wrnh(var_bacg) < 2:
            return 0
        return var_osiz(var_bacg[var_hqta + 1] - var_bacg[var_hqta] for
            var_hqta in var_rgwu(var_wrnh(var_bacg) - 1))
