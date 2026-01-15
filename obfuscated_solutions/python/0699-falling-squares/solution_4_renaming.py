class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(var_rgwu)
        var_wrnh = var_osiz(var_bacg ** 0.5)
        var_ayzf = [0] * var_bacg
        var_wnki = [0] * (var_wrnh + 2)
        var_egyk = [0] * (var_wrnh + 2)

        def func_dcmd(arg_llti, arg_zbxo):
            var_rdmc = 0
            while arg_llti % var_wrnh and arg_llti <= arg_zbxo:
                var_rdmc = var_rjut(var_rdmc, var_ayzf[arg_llti], var_wnki[
                    arg_llti / var_wrnh])
                arg_llti += 1
            while arg_zbxo % var_wrnh != var_wrnh - 1 and arg_llti <= arg_zbxo:
                var_rdmc = var_rjut(var_rdmc, var_ayzf[arg_zbxo], var_wnki[
                    arg_zbxo / var_wrnh])
                arg_zbxo -= 1
            while arg_llti <= arg_zbxo:
                var_rdmc = var_rjut(var_rdmc, var_wnki[arg_llti / var_wrnh],
                    var_egyk[arg_llti / var_wrnh])
                arg_llti += var_wrnh
            return var_rdmc

        def func_lsgw(arg_llti, arg_zbxo, arg_cbvh):
            while arg_llti % var_wrnh and arg_llti <= arg_zbxo:
                var_ayzf[arg_llti] = var_rjut(var_ayzf[arg_llti], arg_cbvh)
                var_egyk[arg_llti / var_wrnh] = var_rjut(var_egyk[arg_llti /
                    var_wrnh], arg_cbvh)
                arg_llti += 1
            while arg_zbxo % var_wrnh != var_wrnh - 1 and arg_llti <= arg_zbxo:
                var_ayzf[arg_zbxo] = var_rjut(var_ayzf[arg_zbxo], arg_cbvh)
                var_egyk[arg_zbxo / var_wrnh] = var_rjut(var_egyk[arg_zbxo /
                    var_wrnh], arg_cbvh)
                arg_zbxo -= 1
            while arg_llti <= arg_zbxo:
                var_wnki[arg_llti / var_wrnh] = var_rjut(var_wnki[arg_llti /
                    var_wrnh], arg_cbvh)
                arg_llti += var_wrnh
        var_yjch = 0
        var_rdmc = []
        for arg_llti, var_dmio in arg_rcsn:
            var_ulfl = var_rgwu[arg_llti]
            var_lgvi = var_rgwu[arg_llti + var_dmio - 1]
            arg_cbvh = func_dcmd(var_ulfl, var_lgvi) + var_dmio
            update(var_ulfl, var_lgvi, arg_cbvh)
            var_yjch = var_rjut(var_yjch, arg_cbvh)
            var_rdmc.append(var_yjch)
        return var_rdmc
