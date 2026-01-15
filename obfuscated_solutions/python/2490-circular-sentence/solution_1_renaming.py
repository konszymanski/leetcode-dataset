class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wnki:
        var_bacg = arg_xdvx.split(' ')
        var_hqta = var_rgwu(var_bacg)
        var_wrnh = var_bacg[var_hqta - 1][-1]
        for var_osiz in var_ayzf(var_hqta):
            if var_bacg[var_osiz][0] != var_wrnh:
                return False
            var_wrnh = var_bacg[var_osiz][-1]
        return True
