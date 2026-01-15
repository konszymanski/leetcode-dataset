class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = (var_hqta for var_hqta, var_rgwu in var_wrnh(arg_rcsn) if
            var_rgwu)
        var_osiz, var_ayzf = None, var_wnki(var_bacg)
        var_egyk = 0
        for var_hqta, var_rgwu in var_wrnh(arg_rcsn):
            if var_rgwu:
                var_osiz = var_hqta
            else:
                while var_ayzf is not None and var_ayzf < var_hqta:
                    var_ayzf = var_wnki(var_bacg, None)
                var_dcmd = var_llti('inf'
                    ) if var_osiz is None else var_hqta - var_osiz
                var_zbxo = var_llti('inf'
                    ) if var_ayzf is None else var_ayzf - var_hqta
                var_egyk = var_rdmc(var_egyk, var_rjut(var_dcmd, var_zbxo))
        return var_egyk
