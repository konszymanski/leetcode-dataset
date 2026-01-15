class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg, var_hqta, var_rgwu = 0, 1, var_wrnh(arg_xdvx)
        while var_hqta < var_rgwu:
            var_osiz = 0
            while var_hqta + var_osiz < var_rgwu and arg_xdvx[var_bacg +
                var_osiz] == arg_xdvx[var_hqta + var_osiz]:
                var_osiz += 1
            if var_hqta + var_osiz < var_rgwu and arg_xdvx[var_bacg + var_osiz
                ] < arg_xdvx[var_hqta + var_osiz]:
                var_bacg, var_hqta = var_hqta, var_ayzf(var_hqta + 1, 
                    var_bacg + var_osiz + 1)
            else:
                var_hqta = var_hqta + var_osiz + 1
        return arg_xdvx[var_bacg:]

    def func_wnki(arg_ihhe, arg_egyk: var_rcsn, arg_dcmd: var_llti) ->var_rcsn:
        if arg_dcmd == 1:
            return arg_egyk
        var_zbxo = arg_ihhe.lastSubstring(arg_egyk)
        var_rgwu, var_rdmc = var_wrnh(arg_egyk), var_wrnh(var_zbxo)
        return var_zbxo[:var_rjut(var_rdmc, var_rgwu - arg_dcmd + 1)]
