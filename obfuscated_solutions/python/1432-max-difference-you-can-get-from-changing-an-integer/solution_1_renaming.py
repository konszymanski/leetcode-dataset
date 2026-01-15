class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:

        def func_bacg(arg_hqta, arg_rgwu):
            return var_wrnh(arg_xdvx).replace(var_wrnh(arg_hqta), var_wrnh(
                arg_rgwu))
        var_osiz = var_ayzf = arg_xdvx
        for arg_hqta in var_wnki(10):
            for arg_rgwu in var_wnki(10):
                var_egyk = func_bacg(arg_hqta, arg_rgwu)
                if var_egyk[0] != '0':
                    var_dcmd = var_rcsn(var_egyk)
                    var_osiz = var_llti(var_osiz, var_dcmd)
                    var_ayzf = var_zbxo(var_ayzf, var_dcmd)
        return var_ayzf - var_osiz
