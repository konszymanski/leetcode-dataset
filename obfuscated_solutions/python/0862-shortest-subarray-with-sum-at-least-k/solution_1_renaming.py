class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = var_ayzf('inf')
        var_wnki = 0
        var_egyk = []
        for var_dcmd, var_llti in var_zbxo(arg_xdvx):
            var_wnki += var_llti
            if var_wnki >= arg_rcsn:
                var_osiz = var_rdmc(var_osiz, var_dcmd + 1)
            while var_egyk and var_wnki - var_egyk[0][0] >= arg_rcsn:
                var_osiz = var_rdmc(var_osiz, var_dcmd - var_rjut(var_egyk)[1])
            var_lsgw(var_egyk, (var_wnki, var_dcmd))
        return -1 if var_osiz == var_ayzf('inf') else var_osiz
