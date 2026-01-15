class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        for var_bacg in var_hqta(1, var_rgwu(arg_rcsn)):
            arg_rcsn[var_bacg] = arg_rcsn[var_bacg - 1] + arg_rcsn[var_bacg]
        var_wrnh = {}
        var_osiz = 0
        for var_bacg in var_hqta(var_rgwu(arg_xdvx)):
            for var_ayzf in arg_xdvx[var_bacg]:
                var_wrnh[var_ayzf] = var_bacg
            var_osiz += var_rgwu(arg_xdvx[var_bacg])
        var_wnki = 'MPG'
        for var_ayzf in var_wnki:
            var_osiz += 0 if var_wrnh.get(var_ayzf, 0) == 0 else arg_rcsn[
                var_wrnh.get(var_ayzf) - 1]
        return var_osiz
