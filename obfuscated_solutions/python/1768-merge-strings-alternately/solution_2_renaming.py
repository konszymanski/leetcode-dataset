class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = []
        var_rgwu = var_wrnh(var_osiz(arg_rcsn), var_osiz(arg_bacg))
        for var_ayzf in var_wnki(var_rgwu):
            if var_ayzf < var_osiz(arg_rcsn):
                var_hqta += arg_rcsn[var_ayzf]
            if var_ayzf < var_osiz(arg_bacg):
                var_hqta += arg_bacg[var_ayzf]
        return ''.join(var_hqta)
