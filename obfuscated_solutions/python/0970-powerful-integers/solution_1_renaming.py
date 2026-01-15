class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_hqta,
        arg_bacg: var_hqta) ->var_rjut[var_hqta]:
        var_rgwu = arg_bacg if arg_xdvx == 1 else var_hqta(var_wrnh(
            arg_bacg, arg_xdvx))
        var_osiz = arg_bacg if arg_rcsn == 1 else var_hqta(var_wrnh(
            arg_bacg, arg_rcsn))
        var_ayzf = var_wnki([])
        for var_egyk in var_dcmd(var_rgwu + 1):
            for var_llti in var_dcmd(var_osiz + 1):
                var_zbxo = arg_xdvx ** var_egyk + arg_rcsn ** var_llti
                if var_zbxo <= arg_bacg:
                    var_ayzf.add(var_zbxo)
                if arg_rcsn == 1:
                    break
            if arg_xdvx == 1:
                break
        return var_rdmc(var_ayzf)
