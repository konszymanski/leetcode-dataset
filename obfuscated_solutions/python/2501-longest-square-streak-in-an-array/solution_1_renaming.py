class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        arg_xdvx.sort()
        var_hqta = var_rgwu()
        var_wrnh = 0
        for var_osiz in arg_xdvx:
            if var_osiz in var_hqta:
                continue
            var_ayzf = var_osiz
            var_wnki = 1
            while var_ayzf * var_ayzf <= 10 ** 5:
                if arg_ihhe._binary_search(arg_xdvx, var_ayzf * var_ayzf):
                    var_ayzf *= var_ayzf
                    var_hqta.add(var_ayzf)
                    var_wnki += 1
                else:
                    break
            var_wrnh = var_egyk(var_wrnh, var_wnki)
        return var_wrnh if var_wrnh >= 2 else -1

    def func_dcmd(arg_ihhe, arg_xdvx: var_rcsn[var_bacg], arg_llti: var_bacg
        ) ->var_cbvh:
        var_zbxo, var_rdmc = 0, var_rjut(arg_xdvx) - 1
        while var_zbxo <= var_rdmc:
            var_lsgw = (var_zbxo + var_rdmc) // 2
            if arg_xdvx[var_lsgw] == arg_llti:
                return True
            elif arg_xdvx[var_lsgw] < arg_llti:
                var_zbxo = var_lsgw + 1
            else:
                var_rdmc = var_lsgw - 1
        return False
