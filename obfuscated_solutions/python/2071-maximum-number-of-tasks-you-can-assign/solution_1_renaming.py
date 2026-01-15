from sortedcontainers import SortedList


class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu[var_wrnh], arg_rcsn:
        var_rgwu[var_wrnh], arg_bacg: var_wrnh, arg_hqta: var_wrnh) ->var_wrnh:
        var_osiz, var_ayzf = var_wnki(arg_xdvx), var_wnki(arg_rcsn)
        arg_xdvx.sort()
        arg_rcsn.sort()

        def func_egyk(arg_dcmd: var_wrnh) ->var_yjch:
            var_llti = arg_bacg
            var_zbxo = var_rdmc(arg_rcsn[var_ayzf - arg_dcmd:])
            for var_rjut in var_lsgw(arg_dcmd - 1, -1, -1):
                if var_zbxo[-1] >= arg_xdvx[var_rjut]:
                    var_zbxo.pop()
                else:
                    if var_llti == 0:
                        return False
                    var_cbvh = var_zbxo.bisect_left(arg_xdvx[var_rjut] -
                        arg_hqta)
                    if var_cbvh == var_wnki(var_zbxo):
                        return False
                    var_llti -= 1
                    var_zbxo.pop(var_cbvh)
            return True
        var_dmio, var_ulfl, var_lgvi = 1, var_wvuc(var_ayzf, var_osiz), 0
        while var_dmio <= var_ulfl:
            arg_dcmd = (var_dmio + var_ulfl) // 2
            if func_egyk(arg_dcmd):
                var_lgvi = arg_dcmd
                var_dmio = arg_dcmd + 1
            else:
                var_ulfl = arg_dcmd - 1
        return var_lgvi
