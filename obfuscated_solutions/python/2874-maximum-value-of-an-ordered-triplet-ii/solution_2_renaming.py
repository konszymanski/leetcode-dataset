class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh, var_osiz, var_ayzf = 0, 0, 0
        for var_wnki in var_egyk(var_hqta):
            var_wrnh = var_dcmd(var_wrnh, var_ayzf * arg_xdvx[var_wnki])
            var_ayzf = var_dcmd(var_ayzf, var_osiz - arg_xdvx[var_wnki])
            var_osiz = var_dcmd(var_osiz, arg_xdvx[var_wnki])
        return var_wrnh
