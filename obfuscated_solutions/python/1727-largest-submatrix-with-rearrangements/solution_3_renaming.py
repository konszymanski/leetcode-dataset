class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_xdvx[0])
        var_osiz = []
        var_ayzf = 0
        for var_wnki in var_egyk(var_hqta):
            var_dcmd = []
            var_llti = [False] * var_wrnh
            for var_zbxo, var_rdmc in var_osiz:
                if arg_xdvx[var_wnki][var_rdmc] == 1:
                    var_dcmd.append((var_zbxo + 1, var_rdmc))
                    var_llti[var_rdmc] = True
            for var_rdmc in var_egyk(var_wrnh):
                if var_llti[var_rdmc] == False and arg_xdvx[var_wnki][var_rdmc
                    ] == 1:
                    var_dcmd.append((1, var_rdmc))
            for var_rjut in var_egyk(var_rgwu(var_dcmd)):
                var_ayzf = var_lsgw(var_ayzf, var_dcmd[var_rjut][0] * (
                    var_rjut + 1))
            var_osiz = var_dcmd
        return var_ayzf
