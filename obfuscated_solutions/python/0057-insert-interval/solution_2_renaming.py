class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_bacg[var_hqta]) ->var_bacg[var_bacg[var_hqta]]:
        if not arg_xdvx:
            return [arg_rcsn]
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = arg_rcsn[0]
        var_ayzf, var_wnki = 0, var_rgwu - 1
        while var_ayzf <= var_wnki:
            var_egyk = (var_ayzf + var_wnki) // 2
            if arg_xdvx[var_egyk][0] < var_osiz:
                var_ayzf = var_egyk + 1
            else:
                var_wnki = var_egyk - 1
        arg_xdvx.insert(var_ayzf, arg_rcsn)
        var_dcmd = []
        for var_llti in arg_xdvx:
            if not var_dcmd or var_dcmd[-1][1] < var_llti[0]:
                var_dcmd.append(var_llti)
            else:
                var_dcmd[-1][1] = var_zbxo(var_dcmd[-1][1], var_llti[1])
        return var_dcmd
