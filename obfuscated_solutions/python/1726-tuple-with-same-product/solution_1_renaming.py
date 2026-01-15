class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        arg_xdvx.sort()
        var_wrnh = 0
        for var_osiz in var_ayzf(var_hqta):
            for var_wnki in var_ayzf(var_hqta - 1, var_osiz, -1):
                var_egyk = arg_xdvx[var_osiz] * arg_xdvx[var_wnki]
                var_dcmd = var_llti()
                for var_zbxo in var_ayzf(var_osiz + 1, var_wnki):
                    if var_egyk % arg_xdvx[var_zbxo] == 0:
                        var_rdmc = var_egyk // arg_xdvx[var_zbxo]
                        if var_rdmc in var_dcmd:
                            var_wrnh += 8
                        var_dcmd.add(arg_xdvx[var_zbxo])
        return var_wrnh
