class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        arg_xdvx.sort()
        var_rgwu = 0
        var_wrnh = 0
        var_osiz = 0
        for var_ayzf in var_wnki(var_egyk(arg_xdvx)):
            var_dcmd = arg_xdvx[var_ayzf]
            var_osiz += var_dcmd
            while (var_ayzf - var_rgwu + 1) * var_dcmd - var_osiz > arg_rcsn:
                var_osiz -= arg_xdvx[var_rgwu]
                var_rgwu += 1
            var_wrnh = var_llti(var_wrnh, var_ayzf - var_rgwu + 1)
        return var_wrnh
