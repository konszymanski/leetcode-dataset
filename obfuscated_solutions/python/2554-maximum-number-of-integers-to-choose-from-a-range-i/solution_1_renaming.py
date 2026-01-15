class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_rgwu) ->var_rgwu:
        arg_xdvx.sort()
        var_wrnh = 0
        for var_osiz in var_ayzf(1, arg_rcsn + 1):
            if arg_ihhe._custom_binary_search(arg_xdvx, var_osiz):
                continue
            arg_bacg -= var_osiz
            if arg_bacg < 0:
                break
            var_wrnh += 1
        return var_wrnh

    def func_wnki(arg_ihhe, arg_egyk: var_hqta[var_rgwu], arg_dcmd: var_rgwu
        ) ->var_lsgw:
        var_llti, var_zbxo = 0, var_rdmc(arg_egyk) - 1
        while var_llti <= var_zbxo:
            var_rjut = (var_llti + var_zbxo) // 2
            if arg_egyk[var_rjut] == arg_dcmd:
                return True
            if arg_egyk[var_rjut] > arg_dcmd:
                var_zbxo = var_rjut - 1
            else:
                var_llti = var_rjut + 1
        return False
