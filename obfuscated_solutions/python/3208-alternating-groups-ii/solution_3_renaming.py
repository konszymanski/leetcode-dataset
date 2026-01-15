class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = 0
        var_ayzf = 1
        var_wnki = arg_xdvx[0]
        for var_egyk in var_dcmd(1, var_rgwu + arg_rcsn - 1):
            var_llti = var_egyk % var_rgwu
            if arg_xdvx[var_llti] == var_wnki:
                var_ayzf = 1
                var_wnki = arg_xdvx[var_llti]
                continue
            var_ayzf += 1
            if var_ayzf >= arg_rcsn:
                var_osiz += 1
            var_wnki = arg_xdvx[var_llti]
        return var_osiz
