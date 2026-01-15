class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_wnki:
        arg_xdvx.sort()
        for var_hqta in var_rgwu(var_wrnh(arg_xdvx)):
            var_osiz = 2 * arg_xdvx[var_hqta]
            var_ayzf = arg_ihhe._custom_binary_search(arg_xdvx, var_osiz)
            if var_ayzf >= 0 and var_ayzf != var_hqta:
                return True
        return False

    def func_egyk(arg_ihhe, arg_xdvx: var_rcsn[var_bacg], var_osiz: var_bacg
        ) ->var_bacg:
        var_dcmd, var_llti = 0, var_wrnh(arg_xdvx) - 1
        while var_dcmd <= var_llti:
            var_zbxo = var_dcmd + (var_llti - var_dcmd) // 2
            if arg_xdvx[var_zbxo] == var_osiz:
                return var_zbxo
            elif arg_xdvx[var_zbxo] < var_osiz:
                var_dcmd = var_zbxo + 1
            else:
                var_llti = var_zbxo - 1
        return -1
