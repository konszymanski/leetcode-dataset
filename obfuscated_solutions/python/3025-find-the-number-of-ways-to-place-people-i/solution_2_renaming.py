class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        arg_xdvx.sort(key=lambda p: (var_hqta[0], -var_hqta[1]))
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = 0
        for var_ayzf in var_wnki(var_rgwu - 1):
            var_egyk = arg_xdvx[var_ayzf][1]
            var_dcmd = var_llti('-inf')
            for var_zbxo in var_wnki(var_ayzf + 1, var_rgwu):
                if arg_xdvx[var_zbxo][1] > var_dcmd and arg_xdvx[var_zbxo][1
                    ] <= var_egyk:
                    var_osiz += 1
                    var_dcmd = arg_xdvx[var_zbxo][1]
        return var_osiz
