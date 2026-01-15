class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]
        ) ->var_bacg:
        var_rgwu = ''.join([(var_wrnh.lower() if var_wrnh.isalnum() else
            ' ') for var_wrnh in arg_xdvx])
        var_osiz = var_rgwu.split()
        var_ayzf = var_wnki(var_egyk)
        var_dcmd = var_llti(arg_rcsn)
        for var_zbxo in var_osiz:
            if var_zbxo not in var_dcmd:
                var_ayzf[var_zbxo] += 1
        return var_rdmc(var_ayzf.items(), key=var_rjut.itemgetter(1))[0]
