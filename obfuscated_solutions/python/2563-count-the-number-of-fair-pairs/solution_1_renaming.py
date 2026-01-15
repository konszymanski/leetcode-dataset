class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        while arg_rcsn <= arg_bacg:
            var_rgwu = arg_rcsn + (arg_bacg - arg_rcsn) // 2
            if arg_xdvx[var_rgwu] >= arg_hqta:
                arg_bacg = var_rgwu - 1
            else:
                arg_rcsn = var_rgwu + 1
        return arg_rcsn

    def func_wrnh(arg_ihhe, arg_xdvx, arg_osiz, arg_ayzf):
        arg_xdvx.sort()
        var_wnki = 0
        for var_egyk in var_dcmd(var_llti(arg_xdvx)):
            arg_rcsn = arg_ihhe.lower_bound(arg_xdvx, var_egyk + 1, 
                var_llti(arg_xdvx) - 1, arg_osiz - arg_xdvx[var_egyk])
            arg_bacg = arg_ihhe.lower_bound(arg_xdvx, var_egyk + 1, 
                var_llti(arg_xdvx) - 1, arg_ayzf - arg_xdvx[var_egyk] + 1)
            var_wnki += arg_bacg - arg_rcsn
        return var_wnki
