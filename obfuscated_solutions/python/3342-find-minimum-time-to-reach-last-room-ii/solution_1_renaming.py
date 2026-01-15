class State:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg):
        arg_ihhe.x = arg_xdvx
        arg_ihhe.y = arg_rcsn
        arg_ihhe.dis = arg_bacg

    def func_hqta(arg_ihhe, arg_rgwu):
        return arg_ihhe.dis < arg_rgwu.dis


class Solution:

    def func_wrnh(arg_ihhe, arg_osiz):
        var_ayzf = var_wnki(arg_osiz)
        var_egyk = var_wnki(arg_osiz[0])
        var_dcmd = var_llti('inf')
        var_zbxo = [([var_dcmd] * var_egyk) for var_rdmc in var_rjut(var_ayzf)]
        var_lsgw = [([0] * var_egyk) for var_rdmc in var_rjut(var_ayzf)]
        var_cbvh = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        var_zbxo[0][0] = 0
        var_yjch = []
        var_dmio.heappush(var_yjch, var_ulfl(0, 0, 0))
        while var_yjch:
            var_lgvi = var_dmio.heappop(var_yjch)
            if var_lsgw[var_lgvi.x][var_lgvi.y]:
                continue
            if var_lgvi.x == var_ayzf - 1 and var_lgvi.y == var_egyk - 1:
                break
            var_lsgw[var_lgvi.x][var_lgvi.y] = 1
            for var_wvuc, var_tufr in var_cbvh:
                var_xhfo, var_miuw = (var_lgvi.x + var_wvuc, var_lgvi.y +
                    var_tufr)
                if not (0 <= var_xhfo < var_ayzf and 0 <= var_miuw < var_egyk):
                    continue
                var_rhvk = var_yybh(var_zbxo[var_lgvi.x][var_lgvi.y],
                    arg_osiz[var_xhfo][var_miuw]) + (var_lgvi.x + var_lgvi.y
                    ) % 2 + 1
                if var_zbxo[var_xhfo][var_miuw] > var_rhvk:
                    var_zbxo[var_xhfo][var_miuw] = var_rhvk
                    var_dmio.heappush(var_yjch, var_ulfl(var_xhfo, var_miuw,
                        var_rhvk))
        return var_zbxo[var_ayzf - 1][var_egyk - 1]
