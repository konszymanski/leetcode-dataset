class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = 0
        for var_ayzf in arg_xdvx:
            var_osiz = (var_osiz + var_ayzf) % arg_rcsn
        var_wnki = var_osiz % arg_rcsn
        if var_wnki == 0:
            return 0
        var_egyk = {(0): -1}
        var_dcmd = 0
        var_llti = var_rgwu
        for var_zbxo in var_rdmc(var_rgwu):
            var_dcmd = (var_dcmd + arg_xdvx[var_zbxo]) % arg_rcsn
            var_rjut = (var_dcmd - var_wnki + arg_rcsn) % arg_rcsn
            if var_rjut in var_egyk:
                var_llti = var_lsgw(var_llti, var_zbxo - var_egyk[var_rjut])
            var_egyk[var_dcmd] = var_zbxo
        return -1 if var_llti == var_rgwu else var_llti
