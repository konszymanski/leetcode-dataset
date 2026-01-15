class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_rcsn)
        var_osiz = [[(0) for var_ayzf in var_wnki(var_wrnh + 1)] for
            var_ayzf in var_wnki(var_hqta + 1)]
        for var_egyk in var_wnki(var_hqta + 1):
            var_osiz[var_egyk][0] = var_egyk
        for var_dcmd in var_wnki(var_wrnh + 1):
            var_osiz[0][var_dcmd] = var_dcmd
        for var_egyk in var_wnki(1, var_hqta + 1):
            for var_dcmd in var_wnki(1, var_wrnh + 1):
                if arg_xdvx[var_egyk - 1] == arg_rcsn[var_dcmd - 1]:
                    var_osiz[var_egyk][var_dcmd] = var_osiz[var_egyk - 1][
                        var_dcmd - 1] + 1
                else:
                    var_osiz[var_egyk][var_dcmd] = var_llti(var_osiz[
                        var_egyk - 1][var_dcmd], var_osiz[var_egyk][
                        var_dcmd - 1]) + 1
        var_zbxo = []
        var_egyk, var_dcmd = var_hqta, var_wrnh
        while var_egyk > 0 and var_dcmd > 0:
            if arg_xdvx[var_egyk - 1] == arg_rcsn[var_dcmd - 1]:
                var_zbxo.append(arg_xdvx[var_egyk - 1])
                var_egyk -= 1
                var_dcmd -= 1
            elif var_osiz[var_egyk - 1][var_dcmd] < var_osiz[var_egyk][
                var_dcmd - 1]:
                var_zbxo.append(arg_xdvx[var_egyk - 1])
                var_egyk -= 1
            else:
                var_zbxo.append(arg_rcsn[var_dcmd - 1])
                var_dcmd -= 1
        while var_egyk > 0:
            var_zbxo.append(arg_xdvx[var_egyk - 1])
            var_egyk -= 1
        while var_dcmd > 0:
            var_zbxo.append(arg_rcsn[var_dcmd - 1])
            var_dcmd -= 1
        return ''.join(var_zbxo[::-1])
