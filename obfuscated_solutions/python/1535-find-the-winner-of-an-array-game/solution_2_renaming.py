class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = arg_xdvx[0]
        var_ayzf = 0
        for var_wnki in var_egyk(1, var_dcmd(arg_xdvx)):
            var_llti = arg_xdvx[var_wnki]
            if var_osiz > var_llti:
                var_ayzf += 1
            else:
                var_osiz = var_llti
                var_ayzf = 1
            if var_ayzf == arg_rcsn or var_osiz == var_rgwu:
                return var_osiz
