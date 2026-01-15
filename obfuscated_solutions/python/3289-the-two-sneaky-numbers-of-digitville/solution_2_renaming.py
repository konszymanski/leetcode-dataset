class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = var_rgwu(arg_xdvx) - 2
        var_wrnh = 0
        for var_osiz in arg_xdvx:
            var_wrnh ^= var_osiz
        for var_ayzf in var_wnki(var_hqta):
            var_wrnh ^= var_ayzf
        var_egyk = var_wrnh & -var_wrnh
        var_dcmd = var_llti = 0
        for var_osiz in arg_xdvx:
            if var_osiz & var_egyk:
                var_dcmd ^= var_osiz
            else:
                var_llti ^= var_osiz
        for var_ayzf in var_wnki(var_hqta):
            if var_ayzf & var_egyk:
                var_dcmd ^= var_ayzf
            else:
                var_llti ^= var_ayzf
        return [var_dcmd, var_llti]
