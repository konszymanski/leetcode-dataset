class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_dcmd:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = var_wrnh(1 for var_osiz in arg_xdvx if var_osiz == 'a')
        var_ayzf = 0
        var_wnki = var_bacg
        for var_osiz in arg_xdvx:
            if var_osiz == 'a':
                var_rgwu -= 1
            var_wnki = var_egyk(var_wnki, var_rgwu + var_ayzf)
            if var_osiz == 'b':
                var_ayzf += 1
        return var_wnki
